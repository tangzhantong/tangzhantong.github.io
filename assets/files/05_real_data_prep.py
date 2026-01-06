import pandas as pd
import os

# ==========================================
# 1. 简化的文件配置 (请确保你已完成重命名)
# ==========================================
DATA_DIR = "../data"
EXPR_FILE = os.path.join(DATA_DIR, "expr_data.txt")  # 对应重命名后的表达量文件
DRUG_FILE = os.path.join(DATA_DIR, "drug_data.xlsx")  # 对应重命名后的 GDSC2_fitted... 文件

TARGET_GENES = ['SLC7A11', 'NQO1', 'NFE2L2']
TARGET_DRUG = 'Sorafenib'


def load_and_process():
    print("🚀 开始读取标准化后的文件名...")

    # --- A. 读取药物数据 (List Format) ---
    print(f"正在读取药物文件: {DRUG_FILE}")
    try:
        # GDSC2_fitted 文件通常第一行就是标题，不需要 header=4
        drug_df = pd.read_excel(DRUG_FILE)
    except Exception as e:
        print(f"❌ 读取失败: {e}")
        return None

    # 自动找"药名"列 (不管是 DRUG_NAME 还是 Drug Name)
    drug_col = None
    for col in drug_df.columns:
        if "drug" in col.lower() and "name" in col.lower():
            drug_col = col
            break

    if drug_col is None:
        print(f"❌ 没找到药名列! 现有列名: {list(drug_df.columns)}")
        return None

    print(f"✅ 锁定药名列: '{drug_col}'")

    # 筛选索拉非尼
    sorafenib_data = drug_df[drug_df[drug_col].str.contains(TARGET_DRUG, case=False, na=False)].copy()
    print(f"   -> 找到 {len(sorafenib_data)} 条 Sorafenib 记录")

    # --- B. 读取表达数据 ---
    print("正在读取表达矩阵 (约 30秒)...")
    expr_df = pd.read_csv(EXPR_FILE, sep='\t')

    # 提取基因
    gene_col = expr_df.columns[0]  # 假设第一列是基因名
    target_expr = expr_df[expr_df[gene_col].isin(TARGET_GENES)].copy()

    # 转置 + 清洗 ID
    target_expr.set_index(gene_col, inplace=True)
    target_expr = target_expr.T
    target_expr.index = target_expr.index.str.replace('DATA.', '', regex=False)
    # 只保留纯数字 ID 的行
    target_expr = target_expr[target_expr.index.str.isnumeric()]
    target_expr.index = target_expr.index.astype(int)

    print(f"   -> 提取了 {target_expr.shape[0]} 个细胞系的表达数据")

    # --- C. 对齐 (Merge) ---
    print("正在合并数据...")
    # 自动找 COSMIC_ID 列
    id_col = None
    for col in sorafenib_data.columns:
        if "cosmic" in col.lower() and "id" in col.lower():
            id_col = col
            break

    if id_col is None:
        print("❌ 无法在药物表中找到 COSMIC_ID 列")
        return None

    merged_df = sorafenib_data.merge(
        target_expr,
        left_on=id_col,
        right_index=True,
        how='inner'
    )

    # 自动找 IC50 列 (通常是 LN_IC50)
    ic50_col = None
    for col in merged_df.columns:
        if "ic50" in col.lower():
            ic50_col = col
            break

    print(f"🎉 处理完成! 最终数据集: {len(merged_df)} 个样本")
    print(f"   - 输入特征: {TARGET_GENES}")
    print(f"   - 预测目标: {ic50_col} (IC50)")

    return merged_df


if __name__ == "__main__":
    if not os.path.exists(DRUG_FILE) or not os.path.exists(EXPR_FILE):
        print("⚠️ 请先按照说明重命名文件：")
        print("   GDSC2_fitted... -> drug_data.xlsx")
        print("   Cell_line...    -> expr_data.txt")
    else:
        final_data = load_and_process()
        if final_data is not None:
            # 保存结果
            out_path = os.path.join(DATA_DIR, "processed", "final_dataset.csv")
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            final_data.to_csv(out_path, index=False)
            print(f"\n✅ 数据已保存至: {out_path}")
            print("下一步：我们可以开始训练真正的模型了！")