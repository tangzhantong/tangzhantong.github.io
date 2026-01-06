import matplotlib.pyplot as plt

# 这是你刚才跑出来的真实数据 (直接硬编码，不需要重跑模型)
DATA = {
    "NQO1": 0.26588,
    "FTH1": 0.08717,
    "KEAP1": 0.04607,
    "NFE2L2": 0.04439,
    "SLC7A11": 0.04242,
    "ACSL4": 0.02789,
    "TFRC": 0.02053,
    "GPX4": 0.01593
}

STAR_GENE = "NQO1"


def draw_svg():
    print("🎨 正在绘制特征重要性 (SVG)...")

    # 排序
    genes_sorted = sorted(DATA, key=DATA.get, reverse=True)
    scores_sorted = [DATA[g] for g in genes_sorted]

    plt.figure(figsize=(10, 6))

    # 颜色设置
    colors = ['#D0021B' if g == STAR_GENE else '#9B9B9B' for g in genes_sorted]

    # 画图
    plt.barh(genes_sorted, scores_sorted, color=colors)
    plt.xlabel('Importance Score (Increase in MSE Loss)', fontsize=12)
    plt.title(f'Feature Importance: {STAR_GENE} is the Driver', fontsize=14)
    plt.gca().invert_yaxis()  # 第一名在最上面

    # 标记
    for i, g in enumerate(genes_sorted):
        if g == STAR_GENE:
            plt.text(scores_sorted[i], i, ' ★ Target', va='center', color='#D0021B', fontweight='bold')

    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()

    # 保存 SVG
    plt.savefig("../feature_importance.svg", format='svg')
    print("✅ 已保存: ../feature_importance.svg")


if __name__ == "__main__":
    draw_svg()