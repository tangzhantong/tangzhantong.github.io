import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
import matplotlib.pyplot as plt
import os

# ==========================================
# 1. 配置 (Config)
# ==========================================
DEVICE = torch.device("cpu")  # M1/M2 可改 "mps"
GENES = ["SLC7A11", "NQO1", "NFE2L2", "GPX4", "ACSL4", "FTH1", "TFRC", "KEAP1"]

# 路径
TRAIN_CSV = "../data/processed/expanded_dataset.csv"
SEQ_PATH = "../data/processed/expanded_seqs.pt"
MODEL_SAVE = "../models/elite8_model.pth"

# 临床数据路径 (使用你之前准备好的 Legacy 数据)
CLINICAL_EXPR = "../data/clinical/legacy_expr.tsv.gz"
CLINICAL_SURV = "../data/clinical/legacy_surv.tsv"


# ==========================================
# 2. 升级版模型结构 (Elite 8 Edition)
# ==========================================
class EliteCNN(nn.Module):
    def __init__(self):
        super(EliteCNN, self).__init__()
        # Input: [Batch, 4, 16000]
        self.conv1 = nn.Conv1d(4, 32, kernel_size=16)
        self.pool1 = nn.MaxPool1d(4, stride=4)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=8)
        self.pool2 = nn.MaxPool1d(4, stride=4)
        self.conv3 = nn.Conv1d(64, 128, kernel_size=4)
        self.pool3 = nn.MaxPool1d(4, stride=4)

        # 计算: 16000 -> 4000 -> 1000 -> 250.
        # 250 * 128 = 32000 (考虑到padding损失，稍微给小一点或者自适应)
        # 这里为了稳妥，我们用一个 AdaptivePool 强制变成固定大小
        self.global_pool = nn.AdaptiveMaxPool1d(200)  # 强制变成 200 长
        self.fc1 = nn.Linear(128 * 200, 512)  # 25600 -> 512

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
        self.fc1 = nn.Linear(8, 64)  # 输入是 8 个基因
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
# 3. 数据集
# ==========================================
class GDSC_Dataset(Dataset):
    def __init__(self, csv_file, seq_file):
        self.df = pd.read_csv(csv_file)
        self.seq = torch.load(seq_file)  # [4, 16000]

        # 表达量
        self.expr = self.df[GENES].values
        self.expr = (self.expr - self.expr.mean(axis=0)) / self.expr.std(axis=0)

        # 标签 (IC50)
        ic50_col = [c for c in self.df.columns if 'IC50' in c][0]
        self.labels = self.df[ic50_col].values

    def __len__(self): return len(self.df)

    def __getitem__(self, i):
        return (self.seq.clone().detach(),
                torch.tensor(self.expr[i], dtype=torch.float32),
                torch.tensor(self.labels[i], dtype=torch.float32))


# ==========================================
# 4. 训练流程
# ==========================================
def train():
    print("🚀 开始训练 Elite-8 模型...")
    ds = GDSC_Dataset(TRAIN_CSV, SEQ_PATH)
    dl = DataLoader(ds, batch_size=32, shuffle=True)

    model = EliteModel().to(DEVICE)
    opt = optim.Adam(model.parameters(), lr=0.0001)  # 降低LR
    loss_fn = nn.MSELoss()

    for epoch in range(50):  # 跑50轮
        total_loss = 0
        for seq, expr, y in dl:
            seq, expr, y = seq.to(DEVICE), expr.to(DEVICE), y.to(DEVICE)
            opt.zero_grad()
            pred = model(seq, expr)
            loss = loss_fn(pred.squeeze(), y)
            loss.backward()
            opt.step()
            total_loss += loss.item()
        if (epoch + 1) % 10 == 0:
            print(f"   Epoch {epoch + 1} | Loss: {total_loss / len(dl):.4f}")

    torch.save(model.state_dict(), MODEL_SAVE)
    print("✅ 模型训练完成！")


# ==========================================
# 5. 临床验证 (TCGA)
# ==========================================
def validate_clinical():
    print("\n🏥 正在进行 TCGA 临床验证...")
    # 1. 读取 Legacy 数据
    surv = pd.read_csv(CLINICAL_SURV, sep='\t')
    if 'sample' in surv.columns:
        surv.set_index('sample', inplace=True)
    elif '_PATIENT' in surv.columns:
        surv.set_index('_PATIENT', inplace=True)

    try:
        expr = pd.read_csv(CLINICAL_EXPR, sep='\t', index_col=0, compression='gzip')
    except:
        expr = pd.read_csv(CLINICAL_EXPR, sep='\t', index_col=0)

    # 2. 筛选 8 个基因
    # 注意: Legacy数据里 KEAP1 可能叫 'KEAP1'，确认基因名是否存在
    available = [g for g in GENES if g in expr.index]
    if len(available) < 8:
        print(f"⚠️ 警告: 只找到了 {len(available)}/8 个基因. 缺失: {set(GENES) - set(available)}")

    df = expr.loc[available].T
    # 补齐缺失基因 (如果缺失用0填充，防止报错)
    for g in GENES:
        if g not in df.columns: df[g] = 0.0

    # 3. 合并
    df = df.join(surv, how='inner')
    df = df.dropna(subset=['OS', 'OS.time'])

    # 4. 预测
    model = EliteModel().to(DEVICE)
    model.load_state_dict(torch.load(MODEL_SAVE))
    model.eval()

    real_seq = torch.load(SEQ_PATH).to(DEVICE)

    # 归一化
    x_data = df[GENES].values
    x_data = (x_data - x_data.mean(axis=0)) / (x_data.std(axis=0) + 1e-6)

    preds = []
    with torch.no_grad():
        for i in range(len(x_data)):
            e_t = torch.tensor([x_data[i]], dtype=torch.float32).to(DEVICE)
            s_t = real_seq.unsqueeze(0)
            score = model(s_t, e_t)
            preds.append(score.item())

    df['Score'] = preds
    med = df['Score'].median()
    high = df[df['Score'] > med]
    low = df[df['Score'] <= med]

    # 5. 统计
    res = logrank_test(high['OS.time'], low['OS.time'], event_observed_A=high['OS'], event_observed_B=low['OS'])
    p_val = res.p_value

    print(f"\n🏆 验证结果 (Elite-8):")
    print(f"   P-value = {p_val:.6f}")
    if p_val < 0.05:
        print("🎉 成功达成目标！显著性差异显著！")
    else:
        print("   虽然未小于0.05，但请观察数值是否比 0.118 更低。")

    # 绘图
    kmf = KaplanMeierFitter()
    plt.figure(figsize=(8, 6))
    kmf.fit(high['OS.time'], high['OS'], label='High Risk')
    kmf.plot_survival_function(color='red')
    kmf.fit(low['OS.time'], low['OS'], label='Low Risk')
    kmf.plot_survival_function(color='blue')
    plt.title(f"Elite-8 Genes Survival Analysis (P={p_val:.4f})")
    plt.savefig("../elite8_survival.png")
    print("   图片已保存至 ../elite8_survival.png")


if __name__ == "__main__":
    train()
    validate_clinical()