import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


# ==========================================
# 1. 搬运模型架构 (确保环境独立)
# ==========================================
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
        feature_vector = torch.relu(self.fc1(x))
        return feature_vector


class PathwayMLP(nn.Module):
    def __init__(self):
        super(PathwayMLP, self).__init__()
        self.fc1 = nn.Linear(3, 16)
        self.fc2 = nn.Linear(16, 8)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return x


class FerroptosisDrugModel(nn.Module):
    def __init__(self):
        super(FerroptosisDrugModel, self).__init__()
        self.cnn_branch = NRF2PromoterCNN()
        self.mlp_branch = PathwayMLP()
        self.fusion_fc1 = nn.Linear(128 + 8, 64)
        self.fusion_fc2 = nn.Linear(64, 1)

    def forward(self, seq_data, expr_data):
        cnn_feat = self.cnn_branch(seq_data)
        mlp_feat = self.mlp_branch(expr_data)
        combined = torch.cat((cnn_feat, mlp_feat), dim=1)
        x = torch.relu(self.fusion_fc1(combined))
        output = self.fusion_fc2(x)
        return output


# ==========================================
# 2. 生成"符合生物学规律"的模拟数据
# ==========================================
def generate_synthetic_data(num_samples=100):
    """
    我们将制造一个规则：
    IC50 (耐药性) = 2.0 * SLC7A11表达量 + 噪音
    这意味着模型必须学会：SLC7A11 越高，药效越差。
    """
    print(f"正在生成 {num_samples} 个模拟样本...")

    # 模拟序列 (随机 DNA)
    seq_data = torch.randn(num_samples, 4, 2000)

    # 模拟表达量 (列0=SLC7A11, 列1=NQO1, 列2=NRF2)
    # 我们让表达量在 0 到 5 之间随机
    expr_data = torch.rand(num_samples, 3) * 5

    # 制造标签 (Label): 真实的 IC50
    # 逻辑：只跟 SLC7A11 (第0列) 有关，跟别的基因没关系
    # y = 2x + 1
    slc7a11_levels = expr_data[:, 0]
    true_ic50 = (slc7a11_levels * 2.0) + 1.0

    # 加上一点随机噪音，模拟真实实验误差
    noise = torch.randn(num_samples) * 0.5
    true_ic50 += noise

    # 调整形状为 [100, 1] 以匹配模型输出
    true_ic50 = true_ic50.unsqueeze(1)

    return seq_data, expr_data, true_ic50


# ==========================================
# 3. 训练循环 (The Training Loop)
# ==========================================
if __name__ == "__main__":
    # A. 准备数据
    seq_train, expr_train, y_train = generate_synthetic_data(num_samples=500)

    # B. 初始化模型、损失函数、优化器
    model = FerroptosisDrugModel()

    # Loss: 均方误差 (MSE)，预测值和真实值差得越远，Loss 越大
    criterion = nn.MSELoss()

    # Optimizer: Adam 优化器，负责调整模型参数来降低 Loss
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print("\n=== 开始训练 (Teaching the AI) ===")
    epochs = 50  # 训练 50 轮

    for epoch in range(epochs):
        # 1. 梯度清零 (PyTorch 规范)
        optimizer.zero_grad()

        # 2. 前向传播 (模型猜结果)
        predictions = model(seq_train, expr_train)

        # 3. 计算损失 (猜得有多离谱？)
        loss = criterion(predictions, y_train)

        # 4. 反向传播 (寻找改进方向)
        loss.backward()

        # 5. 更新参数 (自我修正)
        optimizer.step()

        # 每 10 轮打印一次进度
        if (epoch + 1) % 5 == 0:
            print(f"轮次 [Epoch {epoch + 1}/{epochs}] | 误差 (Loss): {loss.item():.4f}")

    print("\n=== 训练完成 ===")

    # ==========================================
    # 4. 验证时刻：它学会了吗？
    # ==========================================
    print("\n--- 验证测试 ---")
    # 我们造两个极端样本：
    # 样本 A: SLC7A11 极低 (应该敏感，IC50 低)
    # 样本 B: SLC7A11 极高 (应该耐药，IC50 高)

    test_expr = torch.tensor([
        [0.1, 2.0, 2.0],  # 样本 A (低 SLC7A11)
        [5.0, 2.0, 2.0]  # 样本 B (高 SLC7A11)
    ])
    test_seq = torch.randn(2, 4, 2000)  # 序列随机，不影响测试

    model.eval()  # 切换到评估模式
    with torch.no_grad():
        preds = model(test_seq, test_expr)

    print(f"样本 A (SLC7A11 低) 预测 IC50: {preds[0].item():.2f}")
    print(f"样本 B (SLC7A11 高) 预测 IC50: {preds[1].item():.2f}")

    if preds[1] > preds[0]:
        print("✅ 成功！模型学会了 'SLC7A11 导致耐药' 的生物学规则！")
    else:
        print("❌ 失败。模型没看懂数据。")