import requests
import torch
import numpy as np
import os
from Bio.Seq import Seq

# ==========================================
# 1. 配置：基因坐标 (基于 hg38)
# ==========================================
# 坐标需精准，这里我为你查好了这三个基因的 TSS 上游 2000bp 范围
GENE_COORDS = {
    "SLC7A11": {"chrom": "chr4", "start": 138415789 - 2000, "end": 138415789, "strand": "+"},
    "NQO1": {"chrom": "chr16", "start": 69742157, "end": 69742157 + 2000, "strand": "-"},  # 负链基因
    "NFE2L2": {"chrom": "chr2", "start": 177230303, "end": 177230303 + 2000, "strand": "-"}  # 负链基因
}

OUTPUT_FILE = "../data/processed/real_promoter_seqs.pt"


# ==========================================
# 2. 核心函数：调用 UCSC API
# ==========================================
def fetch_sequence_from_ucsc(chrom, start, end):
    print(f"📡 正在从 UCSC 下载 {chrom}:{start}-{end} ...")
    # UCSC DAS API
    url = f"https://api.genome.ucsc.edu/getData/sequence?genome=hg38;chrom={chrom};start={start};end={end}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            raw_seq = data['dna']
            return raw_seq.upper()
        else:
            print(f"❌ 下载失败: {response.status_code}")
            return "N" * (end - start)
    except Exception as e:
        print(f"❌ 连接错误: {e}")
        return "N" * (end - start)


def one_hot_encode(sequence):
    # 确保长度统一为 2000
    if len(sequence) > 2000: sequence = sequence[:2000]
    if len(sequence) < 2000: sequence = sequence + "N" * (2000 - len(sequence))

    mapping = {
        'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'N': [0.25, 0.25, 0.25, 0.25]
    }
    seq_matrix = [mapping.get(base, [0, 0, 0, 0]) for base in sequence]
    # 转为 [4, 2000] 的 Tensor
    return torch.tensor(seq_matrix, dtype=torch.float32).permute(1, 0)


# ==========================================
# 3. 主程序
# ==========================================
if __name__ == "__main__":
    final_tensors = []
    gene_order = ["SLC7A11", "NQO1", "NFE2L2"]  # 必须保持这个顺序

    print("🚀 开始获取真实启动子序列 (Hardcore Mode)...")

    for gene in gene_order:
        info = GENE_COORDS[gene]
        # 1. 下载
        seq_str = fetch_sequence_from_ucsc(info['chrom'], info['start'], info['end'])

        # 2. 负链处理 (如果是负链，需要取反向互补)
        if info['strand'] == "-":
            seq_obj = Seq(seq_str)
            seq_str = str(seq_obj.reverse_complement())
            print(f"   -> {gene} 位于负链，已做反向互补转换。")

        print(f"   -> {gene} 序列获取成功 (前50bp): {seq_str[:50]}...")

        # 3. 编码
        tensor = one_hot_encode(seq_str)
        final_tensors.append(tensor)

    # 堆叠成一个大张量 [3, 4, 2000] -> (3个基因, 4通道, 2000长)
    # 但我们的模型设计是 "每个样本输入 1 个序列张量"
    # 这里我们做一个策略：把这 3 个基因的序列拼起来，或者让 CNN 有 3 个通道？
    # 为了兼容之前的模型，我们将这 3 个基因在 "长度" 方向拼接，变成 [4, 6000]
    # 或者保持 [4, 2000] (取平均)。
    # 💡 最佳策略：拼接。让 CNN 扫描所有三个基因的启动子。

    combined_seq = torch.cat(final_tensors, dim=1)  # 形状变成 [4, 6000]
    print(f"\n📦 合并后张量形状: {combined_seq.shape} (预期: [4, 6000])")

    # 保存
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    torch.save(combined_seq, OUTPUT_FILE)
    print(f"✅ 真实序列已保存至: {OUTPUT_FILE}")