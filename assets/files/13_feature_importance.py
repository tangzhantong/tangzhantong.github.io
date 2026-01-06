import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================================
# 1. 配置与模型定义 (必须与训练时完全一致)
# ==========================================
DEVICE = torch.device("cpu")
GENES = ["SLC7A11", "NQO1", "NFE2L2", "GPX4", "ACSL4", "FTH1", "TFRC", "KEAP1"]
# 你的明星基因
STAR_GENE = "NQO1"

DATA_PATH = "../data/processed/expanded_dataset.csv"
SEQ_PATH = "../data/processed/expanded_seqs.pt"
MODEL_PATH = "../models/elite8_model.pth"


# --- 复制 Elite8 模型结构 ---
class EliteCNN(nn.Module):
    def __init__(self):
        super(EliteCNN, self).__init__()
        self.conv1 = nn.Conv1d(4, 32, kernel_size=16)
        self.pool1 = nn.MaxPool1d(4, stride=4)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=8)
        self.pool2 = nn.MaxPool1d(4, stride=4)
        self.conv3 = nn.Conv1d(64, 128, kernel_size=4)
        self.pool3 = nn.MaxPool1d(4, stride=4)
        self.global_pool = nn.AdaptiveMaxPool1d(200)
        self.fc1 = nn.Linear(128 * 200, 512)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = self.pool1(x)
        x = torch.relu(self.conv2(x))
        x = self.pool2(x)
        x = torch.relu(self.conv3(x))
        x = self.pool3(x)
        x = self.global_pool(x)
        x = x.view(x.size(0), -1)
        return torch.relu(self.fc1(x))


class EliteMLP(nn.Module):
    def __init__(self):
        super(EliteMLP, self).__init__()
        self.fc1 = nn.Linear(8, 64)
        self.fc2 = nn.Linear(64, 32)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return torch.relu(self.fc2(x))


class EliteModel(nn.Module):
    def __init__(self):
        super(EliteModel, self).__init__()
        self.cnn = EliteCNN()
        self.mlp = EliteMLP()
        self.fusion = nn.Linear(512 + 32, 128)
        self.out = nn.Linear(128, 1)

    def forward(self, seq, expr):
        c = self.cnn(seq)
        m = self.mlp(expr)
        combined = torch.cat((c, m), dim=1)
        x = torch.relu(self.fusion(combined))
        return self.out(x)


# ==========================================
# 2. 核心分析逻辑
# ==========================================
def calculate_loss(model, seq, expr, labels, criterion):
    """辅助函数：计算当前数据的 Loss"""
    with torch.no_grad():
        preds = model(seq, expr)
        loss = criterion(preds.squeeze(), labels)
    return loss.item()


def run_feature_importance():
    print(f"🕵️‍♂️ 正在侦查 NQO1 的地位 (以及其他基因)...")

    # 1. 加载数据
    df = pd.read_csv(DATA_PATH)
    real_seq = torch.load(SEQ_PATH).to(DEVICE)  # [4, 16000]

    # 准备 Tensor
    expr_np = df[GENES].values
    # 标准化 (非常重要，否则数值大的基因会天然占优)
    expr_np = (expr_np - expr_np.mean(axis=0)) / expr_np.std(axis=0)

    expr_tensor = torch.tensor(expr_np, dtype=torch.float32).to(DEVICE)

    # 扩展序列以匹配 Batch (这里我们一次性全量预测，或者分批)
    # 为了内存安全，我们分批计算，但为了代码简单，这里GDSC数据量不大(几百)，可以直接全量
    # 序列是同一个 (Reference)，所以我们要 repeat
    seq_batch = real_seq.unsqueeze(0).repeat(len(df), 1, 1)

    ic50_col = [c for c in df.columns if 'IC50' in c][0]
    labels = torch.tensor(df[ic50_col].values, dtype=torch.float32).to(DEVICE)

    # 2. 加载模型
    model = EliteModel().to(DEVICE)
    if os.path.exists(MODEL_PATH):
        model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    else:
        print("❌ 找不到模型文件！")
        return
    model.eval()
    criterion = nn.MSELoss()

    # 3. 计算基准 Loss (Baseline)
    baseline_loss = calculate_loss(model, seq_batch, expr_tensor, labels, criterion)
    print(f"📊 基准 MSE Loss: {baseline_loss:.4f}")

    # 4. 循环置换 (Permutation)
    importance_scores = {}

    for i, gene in enumerate(GENES):
        # 复制一份数据，以免污染原数据
        shuffled_expr = expr_tensor.clone()

        # 核心操作：打乱第 i 列 (即当前基因的数据)
        # 保持列内数据分布不变，但打乱了样本对应关系，破坏了信息
        shuffled_expr[:, i] = shuffled_expr[:, i][torch.randperm(len(df))]

        # 计算新 Loss
        new_loss = calculate_loss(model, seq_batch, shuffled_expr, labels, criterion)

        # 重要性 = Loss 增加了多少
        # 增加越多，说明该基因越重要
        imp = new_loss - baseline_loss
        importance_scores[gene] = imp

        print(f"   -> {gene} 被打乱后，Loss 变动: {imp:+.5f}")

    # 5. 绘图
    genes_sorted = sorted(importance_scores, key=importance_scores.get, reverse=True)
    scores_sorted = [importance_scores[g] for g in genes_sorted]

    plt.figure(figsize=(10, 6))

    # 设置颜色：NQO1 为红色，其他为灰色
    colors = ['#D0021B' if g == STAR_GENE else '#9B9B9B' for g in genes_sorted]

    bars = plt.barh(genes_sorted, scores_sorted, color=colors)
    plt.xlabel('Importance Score (Increase in MSE Loss)', fontsize=12)
    plt.title(f'Feature Importance: Is {STAR_GENE} the Driver?', fontsize=14)
    plt.gca().invert_yaxis()  # 让第一名排在最上面

    # 在 NQO1 旁边加个星号标记
    for i, g in enumerate(genes_sorted):
        if g == STAR_GENE:
            plt.text(scores_sorted[i], i, ' ★ My Target', va='center', color='#D0021B', fontweight='bold')

    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()

    save_path = "../feature_importance.png"
    plt.savefig(save_path, dpi=300)
    print(f"\n✅ 分析完成！重要性排名图已保存至: {save_path}")

    # 打印最终排名
    print("\n🏆 最终排名 (Top 3):")
    for i in range(3):
        print(f"   {i + 1}. {genes_sorted[i]} (Score: {scores_sorted[i]:.5f})")

    if genes_sorted[0] == STAR_GENE:
        print(f"\n✨ 完美！{STAR_GENE} 是模型认为最重要的基因！")
    else:
        rank = genes_sorted.index(STAR_GENE) + 1
        print(f"\n🔍 {STAR_GENE} 排名第 {rank}。")
        print("   (如果不排第一，可能是因为 ACSL4 或 GPX4 的生物学效应太强，或者是 NFE2L2 代替它发挥了作用。)")


if __name__ == "__main__":
    run_feature_importance()