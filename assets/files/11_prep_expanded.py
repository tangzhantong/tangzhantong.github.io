import pandas as pd
import numpy as np
import os
import torch
import requests
from Bio.Seq import Seq

# ==========================================
# 1. 配置：铁死亡 Elite 8 基因坐标 (hg38)
# ==========================================
# 包含了 TSS 上游 2000bp 的大概位置
GENE_META = {
    "SLC7A11": {"chrom": "chr4", "end": 138415789, "strand": "+"},
    "NQO1": {"chrom": "chr16", "end": 69744157, "strand": "-"},
    "NFE2L2": {"chrom": "chr2", "end": 177232303, "strand": "-"},
    "GPX4": {"chrom": "chr19", "end": 1106060, "strand": "-"},  # 核心防御
    "ACSL4": {"chrom": "chrX", "end": 108960200, "strand": "-"},  # 核心驱动
    "FTH1": {"chrom": "chr11", "end": 61957200, "strand": "+"},  # 铁存储
    "TFRC": {"chrom": "chr3", "end": 196049280, "strand": "-"},  # 铁摄入
    "KEAP1": {"chrom": "chr19", "end": 10664600, "strand": "-"}  # NRF2抑制剂
}

# 必须保持固定的顺序
TARGET_GENES = list(GENE_META.keys())
print(f"🛡 目标基因列表 ({len(TARGET_GENES)}个): {TARGET_GENES}")

DATA_DIR = "../data"
EXPR_FILE = os.path.join(DATA_DIR, "expr_data.txt")
DRUG_FILE = os.path.join(DATA_DIR, "drug_data.xlsx")
OUT_CSV = os.path.join(DATA_DIR, "processed", "expanded_dataset.csv")
OUT_SEQ = os.path.join(DATA_DIR, "processed", "expanded_seqs.pt")


# ==========================================
# 2. 序列抓取函数
# ==========================================
def fetch_and_process_seqs():
    print("\n🧬 正在从 UCSC 下载 8 个基因的启动子序列...")
    tensors = []

    for gene in TARGET_GENES:
        info = GENE_META[gene]
        # 定义 2000bp 窗口
        if info['strand'] == "+":
            start, end = info['end'] - 2000, info['end']
        else:
            # 负链基因，TSS在end端，往后取2000 (但在基因组坐标上是+2000)
            # 为了简化，我们统一取坐标点附近的 2000bp
            start, end = info['end'] - 1000, info['end'] + 1000

        url = f"https://api.genome.ucsc.edu/getData/sequence?genome=hg38;chrom={info['chrom']};start={start};end={end}"

        try:
            r = requests.get(url)
            seq_str = r.json()['dna'].upper()
            # 负链取反向互补
            if info['strand'] == "-":
                seq_str = str(Seq(seq_str).reverse_complement())
        except:
            print(f"⚠️ {gene} 下载失败，使用全 N 填充")
            seq_str = "N" * 2000

        # 截断或补全到 2000
        if len(seq_str) > 2000: seq_str = seq_str[:2000]
        if len(seq_str) < 2000: seq_str += "N" * (2000 - len(seq_str))

        # One-hot
        mapping = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'N': [0.25] * 4}
        mat = [mapping.get(b, [0] * 4) for b in seq_str]
        tensors.append(torch.tensor(mat, dtype=torch.float32).permute(1, 0))  # [4, 2000]
        print(f"   -> {gene} Ready.")

    # 拼接所有基因序列: [8个基因, 4通道, 2000bp] -> 拼成 [4, 16000]
    combined = torch.cat(tensors, dim=1)
    torch.save(combined, OUT_SEQ)
    print(f"✅ 序列张量已保存: {combined.shape} (预期 [4, 16000])")


# ==========================================
# 3. 表达量数据提取函数
# ==========================================
def process_expression_data():
    print("\n📊 正在重新提取 8 个基因的表达量与药敏数据...")

    # 1. 药物数据
    drug_df = pd.read_excel(DRUG_FILE)
    # 找药名列
    drug_col = [c for c in drug_df.columns if "drug" in c.lower() and "name" in c.lower()][0]
    sorafenib = drug_df[drug_df[drug_col].str.contains("Sorafenib", case=False, na=False)].copy()

    # 2. 表达量
    expr_df = pd.read_csv(EXPR_FILE, sep='\t')
    gene_col = expr_df.columns[0]
    # 筛选 8 个基因
    target_expr = expr_df[expr_df[gene_col].isin(TARGET_GENES)].copy()

    # 转置清洗
    target_expr.set_index(gene_col, inplace=True)
    target_expr = target_expr.T
    target_expr.index = target_expr.index.str.replace('DATA.', '', regex=False)
    target_expr = target_expr[target_expr.index.str.isnumeric()]
    target_expr.index = target_expr.index.astype(int)

    # 3. 合并
    # 找 ID 列
    id_col = [c for c in sorafenib.columns if "cosmic" in c.lower() and "id" in c.lower()][0]
    merged = sorafenib.merge(target_expr, left_on=id_col, right_index=True, how='inner')

    merged.to_csv(OUT_CSV, index=False)
    print(f"✅ 扩展版数据集已保存: {len(merged)} 样本, 包含 {len(TARGET_GENES)} 个基因特征")


if __name__ == "__main__":
    fetch_and_process_seqs()
    process_expression_data()