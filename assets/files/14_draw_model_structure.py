import matplotlib.pyplot as plt
import matplotlib.patches as patches
import torch
import torch.nn as nn
import os


# ==========================================
# 1. 定义画布风格
# ==========================================
def draw_box(ax, xy, width, height, text, color='#EDF2F7', edge='#4A5568'):
    """画一个圆角矩形代表层/模块"""
    rect = patches.FancyBboxPatch(
        xy, width, height,
        boxstyle="round,pad=0.1",
        linewidth=2,
        edgecolor=edge,
        facecolor=color,
        zorder=2
    )
    ax.add_patch(rect)
    # 添加文字
    cx = xy[0] + width / 2
    cy = xy[1] + height / 2
    ax.text(cx, cy, text, ha='center', va='center', fontsize=10, fontweight='bold', color='#2D3748', zorder=3)
    return rect


def draw_arrow(ax, start, end):
    """画箭头"""
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", lw=2, color='#718096', shrinkA=5, shrinkB=5),
                zorder=1)


# ==========================================
# 2. 绘制主程序
# ==========================================
def visualize_elite_model():
    print("🎨 正在绘制 Elite-8 模型架构图 (Figure 1)...")

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')  # 关掉坐标轴

    # --- 1. 左侧：输入层 ---
    # 序列输入
    draw_box(ax, (0.5, 7.5), 2, 1, "Promoter Sequence\n(One-Hot Matrix)\n[4, 16000]", color='#E6FFFA', edge='#38B2AC')
    # 表达量输入
    draw_box(ax, (0.5, 2.5), 2, 1, "Gene Expression\n(Elite-8 Genes)\n[Batch, 8]", color='#EBF8FF', edge='#4299E1')

    # --- 2. 中间：特征提取层 ---
    # CNN 模块
    draw_box(ax, (3.5, 7.0), 2.5, 2,
             "1D-CNN Module\n\nConv1 (k=16) -> Pool\nConv2 (k=8) -> Pool\nConv3 (k=4) -> Pool\nGlobal MaxPool",
             color='#F0FFF4', edge='#48BB78')
    # MLP 模块
    draw_box(ax, (3.5, 2.5), 2.5, 1, "MLP Module\n\nLinear (8->64)\nReLU\nLinear (64->32)", color='#FAF5FF',
             edge='#9F7AEA')

    # --- 3. 汇聚层 ---
    # 展平与全连接
    draw_box(ax, (7.0, 7.5), 2, 1, "Sequence Feature\nVector\n[512]", color='#FFFFF0', edge='#ECC94B')
    draw_box(ax, (7.0, 2.5), 2, 1, "Pathway Feature\nVector\n[32]", color='#FFFFF0', edge='#ECC94B')

    # Concatenate
    draw_box(ax, (8.0, 5.0), 1.5, 1, "Concatenation\n[512 + 32]", color='#FFFAF0', edge='#ED8936')

    # --- 4. 输出层 ---
    # 最终预测
    draw_box(ax, (8.0, 3.0), 1.5, 0.8, "Final Prediction\n(IC50 Score)", color='#FFF5F5', edge='#F56565')

    # --- 5. 绘制连线 (箭头) ---
    # 序列流
    draw_arrow(ax, (2.6, 8.0), (3.4, 8.0))  # Input -> CNN
    draw_arrow(ax, (6.1, 8.0), (6.9, 8.0))  # CNN -> Feature
    draw_arrow(ax, (8.0, 7.4), (8.75, 6.1))  # Feature -> Concat (折线)

    # 表达量流
    draw_arrow(ax, (2.6, 3.0), (3.4, 3.0))  # Input -> MLP
    draw_arrow(ax, (6.1, 3.0), (6.9, 3.0))  # MLP -> Feature
    draw_arrow(ax, (8.0, 3.6), (8.75, 4.9))  # Feature -> Concat

    # 输出流
    draw_arrow(ax, (8.75, 5.0), (8.75, 3.9))  # Concat -> Output

    # 添加标题
    plt.title("Figure 1: Multimodal Deep Learning Architecture (Elite-8 Model)", fontsize=16, fontweight='bold', y=0.95)
    plt.tight_layout()

    # 保存
    save_path = "../model_architecture.png"
    plt.savefig(save_path, dpi=300)
    # 同时保存 SVG 方便你在论文里调整
    plt.savefig("../model_architecture.svg", format='svg')

    print(f"✅ 模型结构图已生成: {save_path}")
    print("   (包含 PNG 和 SVG 两个版本，SVG 可拖入 PPT/Illustrator 无损编辑)")


if __name__ == "__main__":
    visualize_elite_model()