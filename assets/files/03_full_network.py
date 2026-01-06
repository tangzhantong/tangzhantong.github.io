import torch
import torch.nn as nn
import torch.nn.functional as F


# ==========================================
# 1. 回顾：DNA 序列扫描器 (CNN Branch)
# ==========================================
class NRF2PromoterCNN(nn.Module):
    def __init__(self):
        super(NRF2PromoterCNN, self).__init__()
        self.conv1 = nn.Conv1d(4, 32, kernel_size=10)
        self.pool1 = nn.MaxPool1d(4, stride=4)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=5)
        self.pool2 = nn.MaxPool1d(4, stride=4)

        # 计算卷积后的尺寸：
        # 2000 -> (conv1)1991 -> (pool1)497 -> (conv2)493 -> (pool2)123
        self.flatten_dim = 64 * 123

        # 注意：这里我们去掉最后一层输出 1 的层，
        # 改为输出一个 128 维的"特征向量"，方便后面融合
        self.fc1 = nn.Linear(self.flatten_dim, 128)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = x.view(x.size(0), -1)
        feature_vector = F.relu(self.fc1(x))
        return feature_vector


# ==========================================
# 2. 新增：表达量分析器 (MLP Branch)
# ==========================================
class PathwayMLP(nn.Module):
    def __init__(self):
        super(PathwayMLP, self).__init__()
        # 输入维度: 3 (因为我们重点关注 SLC7A11, NQO1, NFE2L2 这3个基因的表达量)
        self.fc1 = nn.Linear(3, 16)
        self.fc2 = nn.Linear(16, 8)  # 压缩成 8 维的特征向量

    def forward(self, x):
        # x shape: [Batch, 3]
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return x


# ==========================================
# 3. 核心：多模态融合模型 (Hybrid Model)
# ==========================================
class FerroptosisDrugModel(nn.Module):
    def __init__(self):
        super(FerroptosisDrugModel, self).__init__()

        # 实例化两个分支
        self.cnn_branch = NRF2PromoterCNN()
        self.mlp_branch = PathwayMLP()

        # 融合层 (Fusion Layer)
        # 输入 = CNN特征(128) + MLP特征(8) = 136
        self.fusion_fc1 = nn.Linear(128 + 8, 64)
        self.fusion_fc2 = nn.Linear(64, 1)  # 最终输出 IC50 预测值

    def forward(self, seq_data, expr_data):
        # 1. 让 CNN 处理序列
        cnn_feat = self.cnn_branch(seq_data)  # [Batch, 128]

        # 2. 让 MLP 处理表达量
        mlp_feat = self.mlp_branch(expr_data)  # [Batch, 8]

        # 3. 拼接 (Concatenate)
        combined = torch.cat((cnn_feat, mlp_feat), dim=1)  # [Batch, 136]

        # 4. 最终预测
        x = F.relu(self.fusion_fc1(combined))
        output = self.fusion_fc2(x)
        return output


# ==========================================
# 测试数据流
# ==========================================
if __name__ == "__main__":
    # 1. 实例化最终模型
    model = FerroptosisDrugModel()
    print("=== 多模态模型架构 ===")
    print(model)

    # 2. 模拟输入数据 (Batch_size = 4 个样本)
    # 模拟序列数据 (4个样本, ACGT, 2000bp)
    dummy_seq = torch.randn(4, 4, 2000)
    # 模拟表达量数据 (4个样本, 3个基因: SLC7A11, NQO1, NRF2)
    dummy_expr = torch.randn(4, 3)

    # 3. 前向传播
    prediction = model(dummy_seq, dummy_expr)

    print("\n=== 运行结果 ===")
    print(f"输入序列形状: {dummy_seq.shape}")
    print(f"输入表达形状: {dummy_expr.shape}")
    print(f"最终预测 IC50 (形状): {prediction.shape}")
    print(f"预测值示例:\n{prediction.detach().numpy()}")

    print("\n✅ 系统集成成功！模型已具备处理序列和表达量的能力。")