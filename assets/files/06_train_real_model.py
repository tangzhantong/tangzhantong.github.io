import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr
import os

# ==========================================
# 1. 配置与超参数
# ==========================================
DATA_PATH = "../data/processed/final_dataset.csv"
BATCH_SIZE = 32
LEARNING_RATE = 0.001
EPOCHS = 100
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"正在使用计算设备: {DEVICE}")


# ==========================================
# 2. 定义模型架构 (同之前设计)
# ==========================================
class NRF2PromoterCNN(nn.Module):
    def __init__(self):
        super(NRF2PromoterCNN, self).__init__()
        # 输入: 4通道 (ACGT)
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
        feature = torch.relu(self.fc1(x))
        return feature


class PathwayMLP(nn.Module):
    def __init__(self):
        super(PathwayMLP, self).__init__()
        # 输入: 3个基因的表达量
        self.fc1 = nn.Linear(3, 16)
        self.fc2 = nn.Linear(16, 8)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return x


class FerroptosisDrugModel(nn.Module):
    def __init__(self):
        super(FerroptosisDrugModel, self).__init__()
        self.cnn = NRF2PromoterCNN()
        self.mlp = PathwayMLP()
        self.fusion_fc1 = nn.Linear(128 + 8, 64)
        self.fusion_fc2 = nn.Linear(64, 1)

    def forward(self, seq, expr):
        cnn_out = self.cnn(seq)
        mlp_out = self.mlp(expr)
        combined = torch.cat((cnn_out, mlp_out), dim=1)
        x = torch.relu(self.fusion_fc1(combined))
        out = self.fusion_fc2(x)
        return out


# ==========================================
# 3. 数据集加载器 (Custom Dataset)
# ==========================================
class GDSCDataset(Dataset):
    def __init__(self, csv_file, is_train=True):
        # 读取清洗后的 CSV
        self.data = pd.read_csv(csv_file)

        # 归一化表达量 (Z-score normalization)
        # 这一步对深度学习非常重要，防止数值过大导致梯度爆炸
        feat_cols = ['SLC7A11', 'NQO1', 'NFE2L2']
        self.expr_data = self.data[feat_cols].values
        self.expr_data = (self.expr_data - self.expr_data.mean(axis=0)) / self.expr_data.std(axis=0)

        # 读取标签
        # 找到包含 'IC50' 字眼的列
        ic50_col = [c for c in self.data.columns if 'IC50' in c][0]
        self.labels = self.data[ic50_col].values

        # --- 序列数据准备 ---
        # 既然我们用的是"参考基因组"，所有样本对应的基因序列其实是一样的
        # 我们在这里生成一个固定的 SLC7A11 启动子张量供 CNN 使用
        # (在更复杂的模型中，这里会根据 mutation 读取不同的序列)
        print("正在生成基因组序列张量...")
        # 模拟生成一个 One-hot 矩阵 (4, 2000)
        # 真实场景中，这里应该加载 step 01 生成的 .pt 文件
        self.seq_tensor = torch.randn(4, 2000)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # 1. 表达量数据
        expr = torch.tensor(self.expr_data[idx], dtype=torch.float32)

        # 2. 序列数据 (所有样本共享同一个参考序列，作为 Context)
        seq = self.seq_tensor.clone().detach().float()

        # 3. 标签 (IC50)
        label = torch.tensor(self.labels[idx], dtype=torch.float32)

        return seq, expr, label


# ==========================================
# 4. 训练与评估流程
# ==========================================
def train_model():
    # A. 准备数据
    print(f"正在加载数据集: {DATA_PATH}")
    full_dataset = GDSCDataset(DATA_PATH)

    # 拆分训练集 (80%) 和 测试集 (20%)
    train_size = int(0.8 * len(full_dataset))
    test_size = len(full_dataset) - train_size
    train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

    print(f"训练集样本: {len(train_dataset)}, 测试集样本: {len(test_dataset)}")

    # B. 初始化
    model = FerroptosisDrugModel().to(DEVICE)
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
    criterion = nn.MSELoss()  # 回归问题用均方误差

    # C. 训练循环
    print("\n🚀 开始训练...")
    best_corr = -1.0  # 记录最好的相关系数

    for epoch in range(EPOCHS):
        model.train()
        train_loss = 0.0

        for seq, expr, label in train_loader:
            seq, expr, label = seq.to(DEVICE), expr.to(DEVICE), label.to(DEVICE)

            optimizer.zero_grad()
            output = model(seq, expr)
            loss = criterion(output.squeeze(), label)  # squeeze把 [32,1] 变成 [32]
            loss.backward()
            optimizer.step()

            train_loss += loss.item()

        # D. 每个 Epoch 结束后进行测试
        model.eval()
        all_preds = []
        all_labels = []

        with torch.no_grad():
            for seq, expr, label in test_loader:
                seq, expr, label = seq.to(DEVICE), expr.to(DEVICE), label.to(DEVICE)
                output = model(seq, expr)
                all_preds.extend(output.squeeze().cpu().numpy())
                all_labels.extend(label.cpu().numpy())

        # 计算生信核心指标：皮尔逊相关系数 (Pearson R)
        # R 越接近 1，说明预测越准
        pearson_r, _ = pearsonr(all_labels, all_preds)

        if (epoch + 1) % 10 == 0:
            print(
                f"Epoch [{epoch + 1}/{EPOCHS}] | Loss: {train_loss / len(train_loader):.4f} | Test Pearson R: {pearson_r:.4f}")

            # 如果模型进步了，保存一下
            if pearson_r > best_corr:
                best_corr = pearson_r
                torch.save(model.state_dict(), "../models/best_model.pth")

    print(f"\n🏆 训练结束! 最佳测试集相关系数 (R): {best_corr:.4f}")
    print("模型已保存至 ../models/best_model.pth")


if __name__ == "__main__":
    if os.path.exists(DATA_PATH):
        train_model()
    else:
        print(f"❌ 找不到数据文件: {DATA_PATH}，请先运行 05_real_data_prep.py")