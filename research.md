---
layout: default
title: "Research"
lang: en
permalink: /research/
header_style: white
description: "Tang Zhantong's research interests in respiratory diseases, organ-on-a-chip, and in vitro modeling."
---

<style>
/* === Research 页面专用样式 === */
.content-section {
    max-width: 1100px;
    margin: 0 auto 60px auto;
    padding: 0 20px;
}

.project-card {
    margin-bottom: 50px;
    border-bottom: 1px solid var(--color-border-light);
    padding-bottom: 40px;
}

.project-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--color-text-primary);
    margin-bottom: 20px;
    letter-spacing: -0.02em;
    line-height: 1.25;
}

.project-desc {
    font-size: 1.05rem;
    line-height: 1.8;
    color: var(--color-text-secondary);
}

.project-keywords {
    margin-top: 15px;
    font-size: 0.875rem;
    color: var(--color-text-tertiary, #86868b);
    letter-spacing: 0.01em;
}

.project-img {
    width: 100%;
    max-height: 300px;
    object-fit: cover;
    margin-top: 20px;
    border-radius: 4px;
}
</style>

<div class="hero-wrapper">
    <div class="hero-banner" style="background: #1a1a2e; overflow: hidden;">
        <video autoplay muted loop playsinline style="position:absolute;top:50%;left:50%;min-width:100%;min-height:100%;transform:translate(-50%,-50%);object-fit:cover;" poster="/assets/video/bg_poster.jpg" preload="none"><source src="/assets/video/bg.mp4" type="video/mp4"></video>
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1 class="hero-title">Research</h1>
            <div class="hero-subtitle">Respiratory Diseases · In Vitro Modeling · Organ-on-a-Chip</div>
        </div>
    </div>
</div>

<div class="content-section">
    <div class="project-card reveal">
        <h2 class="project-title">1. Modeling Influenza Immune Response in Organ-on-a-Chip</h2>
        <div class="project-desc">
            <p>
                We integrate airway epithelial cells with immune cells in a microfluidic chip and infect the model with influenza virus. The chip lets us measure cytokine production, immune cell migration, and barrier integrity in real time — without animal experiments.
            </p>
            <p class="project-keywords">Organ-on-a-Chip · Influenza · Immune Response · Microfluidics</p>
        </div>
    </div>

    <div class="project-card reveal">
        <h2 class="project-title">2. In Vitro Respiratory Tract Modeling</h2>
        <div class="project-desc">
            <p>
                We grow human airway epithelium at an air-liquid interface (ALI) and in 3D tissue engineering constructs. These models recapitulate mucociliary differentiation and let us test pathogen responses and drug candidates without animal models.
            </p>
            <p class="project-keywords">ALI Culture · 3D Tissue Engineering · Airway Epithelium · Drug Screening</p>
        </div>
    </div>

    <div class="project-card reveal">
        <h2 class="project-title">3. NQO1 and Ferroptosis in Hepatocellular Carcinoma</h2>
        <div class="project-desc">
            <p>
                My undergraduate thesis project. We found NQO1 (NAD(P)H quinone dehydrogenase 1) upregulated in sorafenib-resistant liver cancer cells, where it suppresses ferroptosis through the NRF2–SLC7A11–GPX4 axis. Evidence came from single-cell RNA sequencing and spatial transcriptomics data. The project is now discontinued.
            </p>
            <img src="/assets/images/resis_new.jpg" alt="Sorafenib Resistance" class="project-img">
            <img src="/assets/images/ferr_1.jpg" alt="Ferroptosis Regulation" class="project-img">
            <p class="project-keywords">NQO1 · Ferroptosis · Single-cell RNA-seq · Sorafenib Resistance</p>
        </div>
    </div>
</div>