import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import os

# ==========================================
# 1. 配置与模型定义 (保持不变)
# ==========================================
DATA_PATH = "../data/processed/final_dataset.csv"
MODEL_PATH = "../models/best_model.pth"
DEVICE = torch.device("cpu")


class NRF2PromoterCNN(nn.Module):
    def __init__(self):
        super(NRF2PromoterCNN, self).__init__()
        self.conv1 = nn.Conv1d(4, 32, kernel_size=10)
        self.pool1 = nn.MaxPool1d(4, stride=4)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=5)
        self.pool2 = nn.MaxPool1d(4, stride=4)
        self.flatten_dim = 64 * 123
        self.fc1 = nn.Linear(self.flatten_dim, 128)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = self.pool1(x)
        x = torch.relu(self.conv2(x))
        x = self.pool2(x)
        x = x.view(x.size(0), -1)
        return torch.relu(self.fc1(x))


class PathwayMLP(nn.Module):
    def __init__(self):
        super(PathwayMLP, self).__init__()
        self.fc1 = nn.Linear(3, 16)
        self.fc2 = nn.Linear(16, 8)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return torch.relu(self.fc2(x))


class FerroptosisDrugModel(nn.Module):
    def __init__(self):
        super(FerroptosisDrugModel, self).__init__()
        self.cnn = NRF2PromoterCNN()
        self.mlp = PathwayMLP()
        self.fusion_fc1 = nn.Linear(128 + 8, 64)
        self.fusion_fc2 = nn.Linear(64, 1)

    def forward(self, seq, expr):
        combined = torch.cat((self.cnn(seq), self.mlp(expr)), dim=1)
        x = torch.relu(self.fusion_fc1(combined))
        return self.fusion_fc2(x)


class GDSCDataset(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        feat_cols = ['SLC7A11', 'NQO1', 'NFE2L2']
        self.expr_data = self.data[feat_cols].values
        self.expr_data = (self.expr_data - self.expr_data.mean(axis=0)) / self.expr_data.std(axis=0)
        ic50_col = [c for c in self.data.columns if 'IC50' in c][0]
        self.labels = self.data[ic50_col].values
        self.seq_tensor = torch.randn(4, 2000)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return (self.seq_tensor.clone().detach().float(),
                torch.tensor(self.expr_data[idx], dtype=torch.float32),
                torch.tensor(self.labels[idx], dtype=torch.float32))


# ==========================================
# 2. 绘图主程序 (修改了保存部分)
# ==========================================
def visualize():
    print("🎨 正在加载模型和数据...")
    dataset = GDSCDataset(DATA_PATH)
    loader = DataLoader(dataset, batch_size=32, shuffle=False)

    model = FerroptosisDrugModel()
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model.eval()

    all_preds = []
    all_labels = []

    print("🔮 正在进行全量预测...")
    with torch.no_grad():
        for seq, expr, label in loader:
            output = model(seq, expr)
            all_preds.extend(output.squeeze().numpy())
            all_labels.extend(label.numpy())

    r_value, p_value = pearsonr(all_labels, all_preds)
    print(f"最终确认 Pearson R: {r_value:.4f} (P-value: {p_value:.2e})")

    # --- 设置科研绘图风格 ---
    plt.figure(figsize=(8, 8))
    # 散点颜色使用科研常用的 'RoyalBlue'，设置透明度 alpha 方便看重叠点
    plt.scatter(all_labels, all_preds, alpha=0.6, color='#4169E1', s=40, edgecolor='white', linewidth=0.5)

    min_val = min(min(all_labels), min(all_preds))
    max_val = max(max(all_labels), max(all_preds))
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')

    plt.title(f'Deep Learning Prediction of Sorafenib Response\n(Features: SLC7A11, NQO1, NFE2L2)', fontsize=14)
    plt.xlabel('Actual IC50 (Log-transformed)', fontsize=12)
    plt.ylabel('Predicted IC50 (Model Output)', fontsize=12)

    # 在图中添加相关系数文本
    plt.text(min_val + 0.5, max_val - 1.0, f'Pearson R = {r_value:.3f}\nP < 0.001',
             fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()

    # --- 关键修改：保存为 SVG ---
    svg_path = "../prediction_scatter.svg"
    plt.savefig(svg_path, format='svg', bbox_inches='tight')  # SVG 矢量图
    plt.savefig("../prediction_scatter.png", dpi=300, bbox_inches='tight')  # PNG 预览图

    print(f"\n✅ 图片已保存至:")
    print(f"   1. {svg_path} (矢量图，可用于 Illustrator)")
    print(f"   2. ../prediction_scatter.png (预览图)")
    print("请在左侧项目栏找到 .svg 文件！")


if __name__ == "__main__":
    visualize()