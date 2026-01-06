---
layout: page
title: "🐍Code"
permalink: /code/
---

<style>
  /* 极简折叠框样式 */
  details {
    background-color: #ffffff;
    border-bottom: 1px solid #eee; /* 只保留底边框，更极简 */
    padding: 15px 5px;
  }
  summary {
    cursor: pointer;
    font-size: 18px; /* 字体稍微大一点 */
    font-weight: 500;
    color: #333;
    list-style: none;
    display: flex;
    align-items: center;
    transition: color 0.2s;
  }
  summary:hover {
    color: #0366d6;
  }
  /* 自定义箭头 */
  summary::before {
    content: "+";  /* 用加号代替箭头，更有设计感 */
    font-size: 20px;
    margin-right: 12px;
    color: #999;
    font-weight: normal;
  }
  details[open] summary::before {
    content: "−"; /* 展开变减号 */
  }
  
  /* 文件列表样式 */
  .file-list {
    margin-top: 15px;
    padding-left: 36px; /* 对齐文字 */
  }
  .file-item {
    display: block;
    padding: 8px 0;
    color: #586069;
    text-decoration: none;
    font-size: 15px;
    border-bottom: 1px dashed #f0f0f0;
  }
  .file-item:hover {
    color: #0366d6;
    background-color: #fafafa;
    padding-left: 5px; /* 悬停时微微右移效果 */
    transition: all 0.2s;
  }
  .file-icon {
    margin-right: 8px;
  }
</style>

<div style="margin-bottom: 30px; color: #666;">
  Python 常用分析脚本库
</div>


<details>
<summary>药物敏感性测试 (索拉非尼为例)</summary>

  <div style="padding-left: 36px; margin-bottom: 10px; font-size: 13px; color: #888; font-style: italic;">
    ℹ️ 备注：1.你必须拥有下面的基因表达文件和临床数据（必要时你可自己下载）。
    <a href="/assets/files/legacy_expr.tsv.gz" download style="color: #0366d6; text-decoration: underline; margin-left: 5px;">
      📄 下载基因表达数据legacy_expr.tsv.gz
    </a>
    <a href="/assets/files/legacy_surv.tsv" download style="color: #0366d6; text-decoration: underline; margin-left: 5px;">
      📄 下载临床数据legacy_expr.tsv.gz
    </a>
  </div>

  <div class="file-list">
    <a href="#" class="file-item">
      <td><a href="/assets/files/01_extract_promoter.py" download>📄 01_extract_promoter.py</a></td>
    </a>
    <a href="#" class="file-item">
      <td><a href="/assets/files/02_build_model.py" download>📄 02_build_model.py</a></td>
    </a>
    <a href="#" class="file-item">
      <td><a href="/assets/files/03_full_network.py" download>📄 03_full_network.py</a></td>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/04_train_simulation.py" download>📄 04_train_simulation.py</a></td>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/05_real_data_prep.py" download>📄 05_real_data_prep.py</a></td>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/06_train_real_model.py" download>📄 06_train_real_model.py</a></td>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/07_visualize_results.py" download>📄 07_visualize_results.py</a></td>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/08_fetch_real_dna.py" download>📄 08_fetch_real_dna.py</a></td>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/09_train_hardcore.py" download>📄 09_train_hardcore.py</a></td>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/10_clinical_transfer.py" download>📄 10_clinical_transfer.py</a></td>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/11_prep_expanded.py" download>📄 11_prep_expanded.py</a></td>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/12_train_expanded_clinical.py" download>📄 12_train_expanded_clinical.py</a></td>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/13_feature_importance.py" download>📄 13_feature_importance.py</a></td>
    </a>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/14_draw_model_structure.py" download>📄 14_draw_model_structure.py</a></td>
    </a>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/15_plot_survival_svg.py" download>📄 15_plot_survival_svg.py</a></td>
    </a>
    </a>    <a href="#" class="file-item">
      <td><a href="/assets/files/16_plot_importance_svg.py" download>📄 16_plot_importance_svg.py</a></td>
    </a>
  </div>
</details>

