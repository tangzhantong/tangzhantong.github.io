import torch
import torch.nn as nn
import torch.nn.functional as F


# ==========================================
# 定义 NRF2 启动子扫描网络 (Promoter Scanner)
# ==========================================
class NRF2PromoterCNN(nn.Module):
    def __init__(self):
        super(NRF2PromoterCNN, self).__init__()

        # --- 第一层：卷积层 (Motif Detector) ---
        # 输入通道: 4 (A, C, G, T)
        # 输出通道: 32 (假设我们要学习 32 种不同的转录因子结合模式/Motifs)
        # 卷积核大小: 10 (扫描长度为 10bp 的序列片段，这就对应了 ARE Motif 的典型长度)
        self.conv1 = nn.Conv1d(in_channels=4, out_channels=32, kernel_size=10)

        # --- 第二层：池化层 (Signal Aggregator) ---
        # MaxPool: 在局部区域取最大值，意味着"只要这段区域里有 Motif，不管具体在哪，都记下来"
        self.pool1 = nn.MaxPool1d(kernel_size=4, stride=4)

        # --- 第三层：更多卷积 (Higher-level Features) ---
        # 组合基础 Motif，寻找更复杂的调控语法
        self.conv2 = nn.Conv1d(in_channels=32, out_channels=64, kernel_size=5)
        self.pool2 = nn.MaxPool1d(kernel_size=4, stride=4)

        # --- 全连接层 (Decision Maker) ---
        # 将提取到的序列特征转化为一个"调控潜力分数"
        # 这里的维度计算需要根据输入长度推导，暂时先写死适配 2000bp 的输入
        self.fc1 = nn.Linear(64 * 123, 128)  # 123 是经过两层卷积池化后的长度
        self.fc2 = nn.Linear(128, 1)  # 输出 1 个数值：该启动子对 NRF2 的响应潜力

    def forward(self, x):
        # x shape: [Batch, 4, 2000]

        # 1. 卷积 + 激活 (ReLU 模拟神经元激活)
        x = F.relu(self.conv1(x))
        # 2. 池化
        x = self.pool1(x)

        # 3. 第二轮卷积 + 激活 + 池化
        x = F.relu(self.conv2(x))
        x = self.pool2(x)

        # 4. 展平 (Flatten) -> 准备进入全连接层
        x = x.view(x.size(0), -1)

        # 5. 全连接层 + Dropout (防止过拟合)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        return x


# ==========================================
# 测试模型 (Sanity Check)
# ==========================================
if __name__ == "__main__":
    # 1. 实例化模型
    model = NRF2PromoterCNN()
    print("模型架构已创建:\n", model)

    # 2. 创建一个模拟的输入数据 (Batch_size=2, Channels=4, Length=2000)
    # 模拟两个样本：一个是 SLC7A11，一个是 NQO1
    dummy_input = torch.randn(2, 4, 2000)

    # 3. 试运行 (Forward Pass)
    output = model(dummy_input)

    print("\n--- 试运行结果 ---")
    print(f"输入形状: {dummy_input.shape}")
    print(f"输出形状: {output.shape}")  # 应该输出 [2, 1]
    print(f"预测的'转录潜力值':\n{output.detach().numpy()}")

    print("\n✅ 模型搭建成功！可以处理 2000bp 的启动子序列。")