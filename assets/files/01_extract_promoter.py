import numpy as np
import torch
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import os

# ==========================================
# 1. 配置区域 (Configuration)
# ==========================================
# 在真实研究中，这里应该指向你的 hg38.fa 文件路径
# 例如: GENOME_FASTA_PATH = "../data/genome/hg38.fa"
GENOME_FASTA_PATH = "../data/genome/dummy_genome.fa"
PROMOTER_LENGTH = 2000  # 提取上游 2000bp

# 基因坐标信息 (基于 hg38 参考基因组)
# 注意：真实项目中这些通常来自 GTF/GFF3 注释文件，这里为了演示直接硬编码
GENE_LOCATIONS = {
    "SLC7A11": {
        "chrom": "chr4",
        "tss": 138415789,  # 转录起始位点 (TSS) 示例坐标
        "strand": "+",  # 正链
    },
    "NQO1": {
        "chrom": "chr16",
        "tss": 69742157,  # 示例坐标
        "strand": "-",  # 负链 (注意！负链基因需要特殊处理)
    }
}


# ==========================================
# 2. 辅助函数：生成模拟基因组数据 (仅用于演示)
# ==========================================
def create_dummy_genome_file(filepath):
    """
    如果你还没有下载 3GB 的 hg38.fa，这个函数会创建一个小的模拟文件，
    确保代码可以跑通。
    """
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)

    print(f"正在创建模拟基因组文件: {filepath} ...")

    # 创建模拟的 chr4 和 chr16 序列
    # 随机生成足够的长度覆盖我们的坐标
    records = []

    # 模拟 Chr4 (SLC7A11)
    seq_chr4 = "A" * 138413000 + "ACGT" * 1000 + "T" * 5000  # 简单构造
    # 让我们在 SLC7A11 上游埋一个假冒的 ARE 序列 (TGACTCAGCA) 看看能不能提取到
    # 位置在 TSS (138415789) 上游 100bp 处
    seq_list_4 = ["N"] * 138420000
    # 埋入特定序列以便验证
    target_pos = 138415789 - 100
    seq_list_4[target_pos:target_pos + 10] = list("TGACTCAGCA")
    records.append(SeqRecord(Seq("".join(seq_list_4)), id="chr4", description="Dummy chr4"))

    # 模拟 Chr16 (NQO1)
    seq_list_16 = ["G"] * 70000000
    records.append(SeqRecord(Seq("".join(seq_list_16)), id="chr16", description="Dummy chr16"))

    with open(filepath, "w") as output_handle:
        SeqIO.write(records, output_handle, "fasta")
    print("模拟基因组创建完成。\n")


# ==========================================
# 3. 核心功能：提取序列与 One-Hot 编码
# ==========================================

def get_promoter_seq(genome_dict, chrom, tss, strand, length=2000):
    """
    提取启动子序列。自动处理正负链逻辑。
    """
    if chrom not in genome_dict:
        raise ValueError(f"染色体 {chrom} 不在基因组文件中")

    full_chrom_seq = genome_dict[chrom].seq

    if strand == "+":
        # 正链：取 TSS 上游 (TSS - length 到 TSS)
        start = tss - length
        end = tss
        promoter_seq = full_chrom_seq[start:end]
        print(f"正链提取范围: {start}-{end}")

    elif strand == "-":
        # 负链：基因是从大坐标往小坐标转录的
        # 启动子在 TSS 的"右边" (TSS 到 TSS + length)
        # 并且提取后需要取 反向互补 (Reverse Complement)
        start = tss
        end = tss + length
        raw_seq = full_chrom_seq[start:end]
        promoter_seq = raw_seq.reverse_complement()
        print(f"负链提取范围: {start}-{end} (已做反向互补)")

    else:
        raise ValueError("Strand must be + or -")

    return str(promoter_seq).upper()


def one_hot_encode(sequence):
    """
    将 ACGT 序列转换为 (4, Length) 的 PyTorch 张量
    A: [1,0,0,0], C: [0,1,0,0], G: [0,0,1,0], T: [0,0,0,1]
    """
    mapping = {
        'A': [1, 0, 0, 0],
        'C': [0, 1, 0, 0],
        'G': [0, 0, 1, 0],
        'T': [0, 0, 0, 1],
        'N': [0.25, 0.25, 0.25, 0.25]  # 处理未知碱基，赋予平均概率
    }

    seq_matrix = []
    for base in sequence:
        seq_matrix.append(mapping.get(base, [0, 0, 0, 0]))  # 如果是非法字符，全0

    # 转换为 numpy array 再转 tensor
    # 最终形状: (Length, 4) -> (4, Length) 适合 Conv1D 输入
    np_matrix = np.array(seq_matrix, dtype=np.float32)
    tensor = torch.from_numpy(np_matrix).permute(1, 0)

    return tensor


# ==========================================
# 4. 主程序 (Main Execution)
# ==========================================
if __name__ == "__main__":
    # 步骤 A: 检查并生成模拟数据 (真实场景请注释掉 create_dummy_genome_file)
    if not os.path.exists(GENOME_FASTA_PATH):
        create_dummy_genome_file(GENOME_FASTA_PATH)

    # 步骤 B: 建立基因组索引 (内存高效，不一次性读取整个 3GB 文件)
    print("正在索引基因组 FASTA (这通常很快)...")
    genome_dict = SeqIO.index(GENOME_FASTA_PATH, "fasta")

    # 步骤 C: 循环处理每个基因
    final_dataset = {}

    for gene_name, info in GENE_LOCATIONS.items():
        print(f"--- 处理基因: {gene_name} ---")

        # 1. 提取序列
        seq = get_promoter_seq(genome_dict, info['chrom'], info['tss'], info['strand'], PROMOTER_LENGTH)
        print(f"提取序列 (前50bp): {seq[:50]}...")

        # 2. 转换为 0101 矩阵
        tensor = one_hot_encode(seq)
        print(f"矩阵形状: {tensor.shape}")  # 应该是 [4, 2000]

        final_dataset[gene_name] = tensor
        print("\n")

    # 步骤 D: 查看结果示例 (模拟输入进 CNN 的数据)
    print("=== 完成 ===")
    print(f"SLC7A11 的 PyTorch Tensor 预览 (前 5 列):\n{final_dataset['SLC7A11'][:, :5]}")

    # 你可以保存这个结果供后续训练使用
    # torch.save(final_dataset, "../data/processed/promoter_tensors.pt")