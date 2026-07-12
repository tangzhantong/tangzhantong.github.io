---
layout: default
title: "Research Picks Archive"
lang: en
permalink: /research-picks/
description: "Past weekly GitHub recommendations for scientific writing, biological research, and single-cell analysis."
---

<style>
.archive-container {
    max-width: 900px;
    margin: 90px auto 100px;
    padding: 0 24px;
}

.archive-header {
    margin-bottom: 60px;
}

.archive-back {
    display: inline-block;
    margin-bottom: 22px;
    color: var(--color-text-tertiary) !important;
    font-size: 13px;
    border-bottom: 1px solid transparent;
}

.archive-back:hover {
    color: var(--color-text-primary) !important;
    border-color: var(--color-text-primary);
}

.archive-header h1 {
    margin: 0 0 14px;
    color: var(--color-text-primary);
    font-size: clamp(2.2rem, 5vw, 3.4rem);
    line-height: 1.15;
}

.archive-intro {
    max-width: 680px;
    margin: 0;
    color: var(--color-text-secondary);
    font-size: 17px;
    line-height: 1.7;
}

.archive-week {
    margin-top: 54px;
}

.archive-date {
    margin-bottom: 22px;
    padding-bottom: 12px;
    color: var(--color-text-primary);
    font-family: 'Inter', sans-serif;
    font-size: 1.2rem;
    font-weight: 600;
    border-bottom: 1px solid var(--color-border-light);
}

.archive-list {
    display: grid;
    gap: 14px;
}

.archive-item {
    display: block;
    padding: 22px 24px;
    color: var(--color-text-primary) !important;
    background: var(--color-bg-card);
    border: 1px solid var(--color-border-light);
    border-radius: var(--radius-card);
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
}

.archive-item:hover {
    border-color: var(--color-border);
    box-shadow: 0 5px 16px rgba(0,0,0,0.07);
    transform: translateY(-2px);
    text-decoration: none;
}

.archive-item-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin-bottom: 7px;
}

.archive-item-name {
    font-weight: 600;
}

.archive-item-stars {
    flex: 0 0 auto;
    color: var(--color-text-tertiary);
    font-size: 12px;
}

.archive-item p {
    margin: 0;
    color: var(--color-text-secondary);
    font-size: 14px;
    line-height: 1.6;
}

@media (max-width: 600px) {
    .archive-container {
        margin-top: 60px;
        padding: 0 20px;
    }

    .archive-item {
        padding: 19px 20px;
    }
}
</style>

<div class="archive-container">
    <header class="archive-header">
        <a class="archive-back" href="/">← Back to home</a>
        <h1>Research Picks Archive</h1>
        <p class="archive-intro">A record of useful GitHub projects I have shared for scientific writing, biological research, and single-cell analysis.</p>
    </header>

    <section class="archive-week">
        <h2 class="archive-date">Week of July 6, 2026</h2>
        <div class="archive-list">
            <a class="archive-item" href="https://github.com/bowang-lab/scGPT" target="_blank" rel="noopener noreferrer">
                <div class="archive-item-header">
                    <span class="archive-item-name">scGPT</span>
                    <span class="archive-item-stars">★ 1.6k</span>
                </div>
                <p>A foundation-model codebase for single-cell multi-omics, useful for annotation, perturbation, and representation learning.</p>
            </a>

            <a class="archive-item" href="https://github.com/scverse/squidpy" target="_blank" rel="noopener noreferrer">
                <div class="archive-item-header">
                    <span class="archive-item-name">Squidpy</span>
                    <span class="archive-item-stars">★ 581</span>
                </div>
                <p>Spatial single-cell analysis in Python, covering tissue-neighborhood graphs, spatial statistics, and image features.</p>
            </a>

            <a class="archive-item" href="https://github.com/scverse/cellrank" target="_blank" rel="noopener noreferrer">
                <div class="archive-item-header">
                    <span class="archive-item-name">CellRank</span>
                    <span class="archive-item-stars">★ 454</span>
                </div>
                <p>Fate mapping for multi-view single-cell data with Markov models, RNA velocity, and driver-gene analysis.</p>
            </a>
        </div>
    </section>

    <section class="archive-week">
        <h2 class="archive-date">Week of June 29, 2026</h2>
        <div class="archive-list">
            <a class="archive-item" href="https://github.com/satijalab/seurat" target="_blank" rel="noopener noreferrer">
                <div class="archive-item-header">
                    <span class="archive-item-name">Seurat</span>
                    <span class="archive-item-stars">★ 2.8k</span>
                </div>
                <p>An R toolkit for single-cell genomics, from QC and clustering to integration and annotation.</p>
            </a>

            <a class="archive-item" href="https://github.com/scverse/scanpy" target="_blank" rel="noopener noreferrer">
                <div class="archive-item-header">
                    <span class="archive-item-name">Scanpy</span>
                    <span class="archive-item-stars">★ 2.5k</span>
                </div>
                <p>A scalable Python framework for single-cell analysis across large transcriptomic datasets.</p>
            </a>

            <a class="archive-item" href="https://github.com/scverse/scvi-tools" target="_blank" rel="noopener noreferrer">
                <div class="archive-item-header">
                    <span class="archive-item-name">scvi-tools</span>
                    <span class="archive-item-stars">★ 1.7k</span>
                </div>
                <p>Deep probabilistic models for single-cell and spatial omics analysis in the scverse ecosystem.</p>
            </a>
        </div>
    </section>

    <section class="archive-week">
        <h2 class="archive-date">Week of June 22, 2026</h2>
        <div class="archive-list">
            <a class="archive-item" href="https://github.com/jupyter-book/jupyter-book" target="_blank" rel="noopener noreferrer">
                <div class="archive-item-header">
                    <span class="archive-item-name">Jupyter Book</span>
                    <span class="archive-item-stars">★ 4.3k</span>
                </div>
                <p>Build publication-quality research documents from notebooks and Markdown.</p>
            </a>

            <a class="archive-item" href="https://github.com/sokrypton/ColabFold" target="_blank" rel="noopener noreferrer">
                <div class="archive-item-header">
                    <span class="archive-item-name">ColabFold</span>
                    <span class="archive-item-stars">★ 2.8k</span>
                </div>
                <p>An accessible workflow for protein structure prediction with AlphaFold2.</p>
            </a>

            <a class="archive-item" href="https://github.com/theislab/single-cell-best-practices" target="_blank" rel="noopener noreferrer">
                <div class="archive-item-header">
                    <span class="archive-item-name">Single-Cell Best Practices</span>
                    <span class="archive-item-stars">★ 1.2k</span>
                </div>
                <p>A practical, open guide to single-cell and omics data analysis.</p>
            </a>
        </div>
    </section>
</div>
