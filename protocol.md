---
layout: page
title: "🧪 Protocol"
permalink: /protocol/
---

<div style="text-align: center; margin-bottom: 40px; color: #666; font-style: italic; font-size: 16px;">
  <p>
    protocol有许多是由师姐整理，再此特别感谢！<br>
  </p>
</div>

<style>
  details {
    background-color: #ffffff;
    border-bottom: 1px solid #eee; /* 极简底边框 */
    padding: 15px 5px;
    margin-bottom: 5px;
  }
  summary {
    cursor: pointer;
    font-size: 18px;
    font-weight: 500;
    color: #333;
    list-style: none; /* 隐藏默认三角 */
    display: flex;
    align-items: center;
    transition: color 0.2s;
  }
  summary:hover {
    color: #27ae60; /* 鼠标悬停变绿色，呼应 Protocol 的主题色 */
  }
  
  /* 自定义加号/减号图标 */
  summary::before {
    content: "+";
    font-size: 20px;
    margin-right: 12px;
    color: #999;
    font-weight: normal;
  }
  details[open] summary::before {
    content: "−";
  }

  /* PDF 文件链接样式 */
  .pdf-link {
    display: block;
    padding: 10px 0 10px 36px; /* 缩进对齐 */
    color: #586069;
    text-decoration: none;
    border-bottom: 1px dashed #f0f0f0; /* 虚线分隔 */
    font-size: 15px;
  }
  .pdf-link:hover {
    color: #27ae60; /* 悬停变绿 */
    background-color: #fafafa;
  }
  .icon { margin-right: 8px; }
</style>

<details>
<summary>🧫 细胞实验 (Cell Experiments)</summary>
  <div style="margin-top: 10px;">
    <a href="/assets/protocol/cell_culture.pdf" class="pdf-link" download>
      <span class="icon">📄</span> 细胞复苏、传代及冻存标准流程.pdf 
    </a>
    <a href="/assets/protocol/cell_phenotype.pdf" class="pdf-link">
      <span class="icon">📄</span> 细胞表型实验.pdf 
    </a>
    <a href="/assets/protocol/ROS.pdf" class="pdf-link">
      <span class="icon">📄</span> 脂质过氧化检测.pdf 
    </a>
  </div>
</details>

<details>
<summary>🧬 分子实验 (Molecular Experiments)</summary>
  <div style="margin-top: 10px;">
    <a href="/assets/protocol/western_blot.pdf" class="pdf-link">
      <span class="icon">📄</span> Western Blot 详细步骤.pdf 
    </a>
    <a href="/assets/protocol/extractRNA_re_qPCR.pdf" class="pdf-link">
      <span class="icon">📄</span> RNA 提取与逆转录 (RT-qPCR).pdf 
    </a>
    <a href="/assets/protocol/extract_plasmid.pdf" class="pdf-link">
      <span class="icon">📄</span> 质粒抽提与转化.pdf 
    </a>
    <a href="/assets/protocol/nu_cy.pdf" class="pdf-link">
      <span class="icon">📄</span> 核质分离.pdf 
    </a>
  </div>
</details>

<details>
<summary>🐁 动物实验 (Animal Experiments)</summary>
  <div style="margin-top: 10px;">
    <a href="/assets/protocol/animal_tumor.pdf" class="pdf-link">
      <span class="icon">📄</span> c57皮下成瘤模型构建.pdf 
    </a>
  </div>
</details>

<details>
  <summary>💻 常用的生物学网站</summary>
  
  <div style="margin-top: 10px; padding-left: 5px;">
    
    <div style="margin-bottom: 8px;">
      <a href="https://www.ncbi.nlm.nih.gov/" target="_blank" style="text-decoration: none;">
        <span class="icon">🌐</span> NCBI (综合数据库)
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" style="text-decoration: none;">
        <span class="icon">🌐</span> PubMed (文献检索)
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://www.addgene.org/" target="_blank" style="text-decoration: none;">
        <span class="icon">🧬</span> Addgene (质粒库)
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://genome.ucsc.edu/" target="_blank" style="text-decoration: none;">
        <span class="icon">🧬</span> UCSC Genome Browser
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://portal.gdc.cancer.gov/" target="_blank" style="text-decoration: none;">
        <span class="icon">📊</span> GDC Data Portal (TCGA)
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://www.ncbi.nlm.nih.gov/geo/" target="_blank" style="text-decoration: none;">
        <span class="icon">📊</span> GEO
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="http://gepia2.cancer-pku.cn/" target="_blank" style="text-decoration: none;">
        <span class="icon">📈</span> GEPIA2 (表达与生存)
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://string-db.org/" target="_blank" style="text-decoration: none;">
        <span class="icon">🕸️</span> STRING (蛋白互作)
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://metascape.org/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> Metascape (富集分析)
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://jaspar.elixir.no/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> JASPAR (转录因子结合motif分析及启动子scan)
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://www.origene.com/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> qPCR引物一键查找
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://www.cellbank.org.cn/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> 中科院cellbank
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://bio-protocol.org/cn" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> bio-protocol
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://www.nature.com/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> Nature
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://www.cell.com/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> Cell
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://www.science.org/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> Science
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://bioart.niaid.nih.gov/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> Bioart(用于生物绘图的素材)
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://app.biorender.com/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> Bio-render
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://app.biorender.com/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> Bio-render
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://www.cancerrxgene.org/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> GDSC耐药数据库
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://parasite.wormbase.org/index.html" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> 寄生虫数据库
      </a>
    </div>

    <div style="margin-bottom: 8px;">
      <a href="https://services.healthtech.dtu.dk/services/NetPhos-3.1/" target="_blank" style="text-decoration: none;">
        <span class="icon">🔍</span> 预测磷酸化位点
      </a>
    </div>

    </div>
</details>