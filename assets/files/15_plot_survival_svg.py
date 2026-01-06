import torch
import torch.nn as nn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
import os

# ==========================================
# 1. 配置
# ==========================================
DEVICE = torch.device("cpu")
GENES = ["SLC7A11", "NQO1", "NFE2L2", "GPX4", "ACSL4", "FTH1", "TFRC", "KEAP1"]

MODEL_PATH = "../models/elite8_model.pth"
SEQ_PATH = "../data/processed/expanded_seqs.pt"
CLINICAL_EXPR = "../data/clinical/legacy_expr.tsv.gz"
CLINICAL_SURV = "../data/clinical/legacy_surv.tsv"


# ==========================================
# 2. 必须重新定义模型结构 (为了加载权重)
# ==========================================
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
# 3. 绘图主程序
# ==========================================
def plot_svg():
    print("🎨 正在重新绘制生存曲线 (SVG)...")

    # 1. 加载数据
    surv = pd.read_csv(CLINICAL_SURV, sep='\t')
    if 'sample' in surv.columns:
        surv.set_index('sample', inplace=True)
    elif '_PATIENT' in surv.columns:
        surv.set_index('_PATIENT', inplace=True)

    try:
        expr = pd.read_csv(CLINICAL_EXPR, sep='\t', index_col=0, compression='gzip')
    except:
        expr = pd.read_csv(CLINICAL_EXPR, sep='\t', index_col=0)

    available = [g for g in GENES if g in expr.index]
    df = expr.loc[available].T
    for g in GENES:
        if g not in df.columns: df[g] = 0.0

    df = df.join(surv, how='inner')
    df = df.dropna(subset=['OS', 'OS.time'])

    # 2. 加载模型
    model = EliteModel().to(DEVICE)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model.eval()
    real_seq = torch.load(SEQ_PATH, map_location=DEVICE)

    # 3. 预测
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

    # 4. 统计与绘图
    results = logrank_test(high['OS.time'], low['OS.time'], event_observed_A=high['OS'], event_observed_B=low['OS'])
    p_val = results.p_value

    plt.figure(figsize=(8, 6))
    kmf = KaplanMeierFitter()

    kmf.fit(high['OS.time'], high['OS'], label='High Resistance Risk')
    kmf.plot_survival_function(color='#D0021B', linewidth=2)  # 红色

    kmf.fit(low['OS.time'], low['OS'], label='Low Resistance Risk')
    kmf.plot_survival_function(color='#4A90E2', linewidth=2)  # 蓝色

    plt.title(f"Elite-8 Genes Survival Analysis (P={p_val:.4f})", fontsize=14)
    plt.xlabel("Days", fontsize=12)
    plt.ylabel("Survival Probability", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.3)

    # 保存 SVG
    plt.savefig("../elite8_survival.svg", format='svg')
    print(f"✅ 已保存: ../elite8_survival.svg (P={p_val:.4f})")


if __name__ == "__main__":
    plot_svg()