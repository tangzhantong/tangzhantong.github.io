import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
import os


# ==========================================
# 1. 模型结构 (保持不变)
# ==========================================
class HardcoreCNN(nn.Module):
    def __init__(self):
        super(HardcoreCNN, self).__init__()
        self.conv1 = nn.Conv1d(4, 32, kernel_size=12)
        self.pool1 = nn.MaxPool1d(4, stride=4)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=6)
        self.pool2 = nn.MaxPool1d(4, stride=4)
        self.conv3 = nn.Conv1d(64, 128, kernel_size=3)
        self.pool3 = nn.MaxPool1d(4, stride=4)
        self.fc1 = nn.Linear(11776, 256)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = self.pool1(x)
        x = torch.relu(self.conv2(x))
        x = self.pool2(x)
        x = torch.relu(self.conv3(x))
        x = self.pool3(x)
        x = x.view(x.size(0), -1)
        return torch.relu(self.fc1(x))


class PathwayMLP(nn.Module):
    def __init__(self):
        super(PathwayMLP, self).__init__()
        self.fc1 = nn.Linear(3, 32)
        self.fc2 = nn.Linear(32, 16)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return torch.relu(self.fc2(x))


class HardcoreModel(nn.Module):
    def __init__(self):
        super(HardcoreModel, self).__init__()
        self.cnn = HardcoreCNN()
        self.mlp = PathwayMLP()
        self.fusion_fc1 = nn.Linear(256 + 16, 128)
        self.fusion_fc2 = nn.Linear(128, 1)

    def forward(self, seq, expr):
        cnn_out = self.cnn(seq)
        mlp_out = self.mlp(expr)
        combined = torch.cat((cnn_out, mlp_out), dim=1)
        x = torch.relu(self.fusion_fc1(combined))
        return self.fusion_fc2(x)


# ==========================================
# 2. 文件路径配置
# ==========================================
MODEL_PATH = "../models/hardcore_model.pth"
SEQ_PATH = "../data/processed/real_promoter_seqs.pt"

# 表达量数据：刚才下的 IlluminaHiSeq (应该是 .gz 压缩包)
EXPR_FILE = "../data/clinical/legacy_expr.tsv.gz"
# 生存数据：刚才 Ctrl+S 保存的纯文本 (去掉 .gz)
SURV_FILE = "../data/clinical/legacy_surv.tsv"


# ==========================================
# 3. 核心处理逻辑
# ==========================================
def prepare_patient_data():
    print("🧹 正在读取 TCGA Legacy 数据...")

    if not os.path.exists(EXPR_FILE):
        print(f"❌ 找不到表达量文件: {EXPR_FILE}")
        return None
    if not os.path.exists(SURV_FILE):
        print(f"❌ 找不到生存数据文件: {SURV_FILE}")
        print("   -> 请确保你已将网页内容保存为 'legacy_surv.tsv' (不带 .gz)")
        return None

    # 1. 读取生存数据 (纯文本模式)
    try:
        surv_df = pd.read_csv(SURV_FILE, sep='\t')
    except Exception as e:
        print(f"❌ 读取生存数据失败: {e}")
        return None

    # 处理索引列 (通常是 'sample' 或 '_PATIENT')
    if 'sample' in surv_df.columns:
        surv_df = surv_df.set_index('sample')
    elif '_PATIENT' in surv_df.columns:  # Legacy数据有时用这个名字
        surv_df = surv_df.set_index('_PATIENT')

    # 2. 读取表达量 (压缩包模式)
    print("   -> 读取表达量矩阵 (Legacy)...")
    try:
        expr_df = pd.read_csv(EXPR_FILE, sep='\t', index_col=0, compression='gzip')
    except:
        print("   ⚠️ 尝试作为纯文本读取表达量...")
        expr_df = pd.read_csv(EXPR_FILE, sep='\t', index_col=0)

    # 3. 筛选基因
    target_genes = ['SLC7A11', 'NQO1', 'NFE2L2']
    missing = [g for g in target_genes if g not in expr_df.index]
    if missing:
        print(f"❌ 警告：未找到基因 {missing}，可能是数据版本问题。")
        return None

    filtered_expr = expr_df.loc[target_genes].T

    # 4. 合并 (自动对齐 Sample ID)
    final_df = filtered_expr.join(surv_df, how='inner')

    # 确保有生存时间 (OS.time) 和 状态 (OS)
    if 'OS.time' not in final_df.columns or 'OS' not in final_df.columns:
        print("❌ 数据中缺少 OS.time 或 OS 列")
        print(f"   现有列名: {final_df.columns}")
        return None

    # 去除缺失值
    final_df = final_df.dropna(subset=['OS', 'OS.time'] + target_genes)

    print(f"✅ 清洗完成！成功匹配 {len(final_df)} 位病人。")
    return final_df


def predict_risk_and_plot(df):
    print("🔮 AI 正在进行临床风险预测...")

    model = HardcoreModel()
    model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
    model.eval()

    real_seq = torch.load(SEQ_PATH, map_location=torch.device('cpu'))

    predictions = []
    expr_data = df[['SLC7A11', 'NQO1', 'NFE2L2']].values
    # 归一化
    expr_data = (expr_data - expr_data.mean(axis=0)) / expr_data.std(axis=0)

    with torch.no_grad():
        for i in range(len(expr_data)):
            expr_tensor = torch.tensor([expr_data[i]], dtype=torch.float32)
            seq_tensor = real_seq.unsqueeze(0)
            risk_score = model(seq_tensor, expr_tensor)
            predictions.append(risk_score.item())

    df['Risk_Score'] = predictions

    # 分组 (高/低风险)
    median_score = df['Risk_Score'].median()
    high_risk = df[df['Risk_Score'] > median_score]
    low_risk = df[df['Risk_Score'] <= median_score]

    print(f"   -> 高风险组: {len(high_risk)} 人 (Predicted Resistant)")
    print(f"   -> 低风险组: {len(low_risk)} 人 (Predicted Sensitive)")

    # 绘图
    kmf = KaplanMeierFitter()
    plt.figure(figsize=(10, 6))

    kmf.fit(high_risk['OS.time'], high_risk['OS'], label='High Resistance Risk')
    kmf.plot_survival_function(color='#D0021B', linewidth=2)

    kmf.fit(low_risk['OS.time'], low_risk['OS'], label='Low Resistance Risk')
    kmf.plot_survival_function(color='#4A90E2', linewidth=2)

    results = logrank_test(high_risk['OS.time'], low_risk['OS.time'],
                           event_observed_A=high_risk['OS'], event_observed_B=low_risk['OS'])

    p_val = results.p_value
    plt.title(f"AI-Predicted Survival Stratification (TCGA-LIHC)\nLog-rank P = {p_val:.4f}", fontsize=14)
    plt.xlabel("Survival Time (Days)", fontsize=12)
    plt.ylabel("Survival Probability", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.3)

    # 保存结果
    plt.savefig("../tcga_survival_curve.png", dpi=300)
    plt.savefig("../tcga_survival_curve.svg", format='svg')  # 矢量图
    print(f"\n🏆 最终成果已生成！")
    print(f"   P-value: {p_val:.5f}")
    print(f"   图片路径: ../tcga_survival_curve.png")


if __name__ == "__main__":
    df = prepare_patient_data()
    if df is not None:
        predict_risk_and_plot(df)