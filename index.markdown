---
layout: default
title: Home
lang: en
permalink: /
header_style: white
description: "Tang Zhantong's personal website - Committed to reducing dependence on and harm to experimental animals through innovative in vitro models."
---

<style>
/* --- 首页专用样式（不含公共 Hero/Nav，已提取到 SCSS） --- */

/* NEWS 区域 */
.content-container {
    max-width: 1100px;
    margin: 60px auto;
    padding: 0 20px;
}

.section-title {
    text-align: center;
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--color-text-primary);
    margin-bottom: 50px;
    letter-spacing: -0.02em;
}

.news-list {
    list-style: none;
    padding: 0 16px 0 0;
    margin: 0;
    max-height: 520px;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: var(--color-border) transparent;
}

.news-list::-webkit-scrollbar {
    width: 8px;
}

.news-list::-webkit-scrollbar-track {
    background: transparent;
}

.news-list::-webkit-scrollbar-thumb {
    background-color: var(--color-border);
    border-radius: 4px;
}

.news-list::-webkit-scrollbar-thumb:hover {
    background-color: var(--color-text-tertiary);
}

.news-item {
    display: flex;
    align-items: flex-start;
    padding: 20px 0;
    border-bottom: 1px solid var(--color-border-light);
    font-size: 16px;
    line-height: 1.8;
}

.news-item:first-child {
    padding-top: 0;
}

.news-date {
    font-weight: 600;
    color: var(--color-text-tertiary);
    min-width: 130px;
    margin-right: 30px;
    font-family: monospace;
}

.news-content {
    color: var(--color-text-secondary);
}

/* --- About Me 区域 --- */
.about-section {
    max-width: 1100px;
    margin: 80px auto 60px;
    padding: 0 20px;
    display: flex;
    gap: 40px;
    align-items: center;
}

.about-photo {
    flex-shrink: 0;
}

.about-photo img {
    width: 180px;
    height: 180px;
    border-radius: 0;
    object-fit: cover;
}

.about-text h2 {
    font-size: 1.6rem;
    margin-bottom: 12px;
    color: var(--color-text-primary);
    letter-spacing: -0.02em;
}

.about-text p {
    font-size: 15px;
    line-height: 1.8;
    color: var(--color-text-secondary);
    margin-bottom: 10px;
}

.about-links {
    display: flex;
    gap: 10px 20px;
    margin-top: 18px;
    flex-wrap: wrap;
}

.about-links a {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 0 0 3px;
    border-bottom: 1px solid transparent;
    font-size: 13px;
    color: var(--color-text-secondary) !important;
    transition: color 0.2s ease, border-color 0.2s ease;
}

.about-links a:hover {
    color: var(--color-text-primary) !important;
    border-color: var(--color-text-primary);
}

/* --- Research Highlights --- */
.highlights-section {
    max-width: 1100px;
    margin: 0 auto 80px;
    padding: 0 20px;
}

.highlights-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 0;
    margin-top: 30px;
    border-top: 1px solid var(--color-border-light);
    border-bottom: 1px solid var(--color-border-light);
}

.highlight-card {
    padding: 34px 30px;
    border-right: 1px solid var(--color-border-light);
    text-align: left;
}

.highlight-card:last-child {
    border-right: 0;
}

.highlight-icon {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 20px;
}

.highlight-card h3 {
    font-size: 1rem;
    margin-bottom: 8px;
    color: var(--color-text-primary);
}

.highlight-card p {
    font-size: 13px;
    color: var(--color-text-secondary);
    line-height: 1.6;
}

/* --- Shared Resources --- */
.resources-section {
    max-width: 1100px;
    margin: -30px auto 80px;
    padding: 0 20px;
}

.resources-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 28px;
}

.resource-panel {
    min-width: 0;
}

.resource-heading {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 16px;
}

.resource-heading .section-title {
    margin-bottom: 0;
}

.resource-archive-link {
    flex: 0 0 auto;
    color: var(--color-text-tertiary) !important;
    font-size: 12px;
    letter-spacing: 0.02em;
    border-bottom: 1px solid transparent;
    transition: color 0.2s ease, border-color 0.2s ease;
}

.resource-archive-link:hover {
    color: var(--color-text-primary) !important;
    border-color: var(--color-text-primary);
}

.resource-card {
    display: flex;
    align-items: center;
    gap: 22px;
    margin-top: 30px;
    min-height: 176px;
    padding: 28px 0;
    border-top: 1px solid var(--color-border-light);
    border-bottom: 1px solid var(--color-border-light);
}

.resource-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    flex: 0 0 58px;
    width: 58px;
    height: 58px;
    border-radius: 0;
    background: transparent;
}

.resource-content h3 {
    margin: 0 0 7px;
    font-size: 1.05rem;
    color: var(--color-text-primary);
}

.resource-content p {
    margin: 0;
    color: var(--color-text-secondary);
    line-height: 1.7;
}

.resource-book-title {
    font-style: italic;
    color: var(--color-text-primary);
}

.github-picks {
    display: grid;
    gap: 0;
    margin-top: 30px;
    border-top: 1px solid var(--color-border-light);
}

.github-pick {
    display: block;
    padding: 18px 0;
    border-bottom: 1px solid var(--color-border-light);
    transition: color 0.2s ease;
}

.github-pick:hover {
    text-decoration: none;
}

.github-pick:hover .github-pick-name {
    color: var(--color-link);
}

.github-pick-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 5px;
}

.github-pick-name {
    color: var(--color-text-primary);
    font-size: 0.95rem;
    font-weight: 600;
}

.github-pick-stars {
    flex: 0 0 auto;
    color: var(--color-text-tertiary);
    font-size: 12px;
}

.github-pick p {
    margin: 0;
    color: var(--color-text-secondary);
    font-size: 13px;
    line-height: 1.55;
}

/* 移动端 */
@media (max-width: 768px) {
    .about-section {
        flex-direction: column;
        text-align: center;
    }
    .about-links {
        justify-content: center;
    }
    .resource-card {
        align-items: flex-start;
        padding: 24px 22px;
    }
    .resources-grid {
        grid-template-columns: 1fr;
        gap: 50px;
    }
    .highlights-grid {
        grid-template-columns: 1fr;
    }
    .highlight-card {
        border-right: 0;
        border-bottom: 1px solid var(--color-border-light);
        padding-left: 0;
        padding-right: 0;
    }
    .highlight-card:last-child {
        border-bottom: 0;
    }
}
</style>

<div class="video-container">
    <video autoplay muted loop playsinline id="bg-video" poster="/assets/video/bg_poster.jpg" preload="none">
        <source src="/assets/video/bg.mp4" type="video/mp4">
        Your browser does not support HTML5 video.
    </video>
    <div class="video-overlay"></div>
    <div class="video-content">
        <h1 class="hero-title">Less Animal Testing.</h1>
        <p class="hero-video-subtitle">Better Human Medicine.<br><span>Microfluidic organ-on-a-chip models for respiratory disease research.</span></p>
    </div>
    <div class="scroll-indicator">
        <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><polyline points="7 13 12 18 17 13"/><line x1="12" y1="6" x2="12" y2="18"/></svg>
    </div>
</div>

<!-- About Me -->
<div class="about-section reveal">
    <div class="about-photo">
        <img src="/assets/images/tang_selfish.png" alt="Tang Zhantong portrait" loading="lazy">
    </div>
    <div class="about-text">
        <h2>About Me</h2>
        <p>Hi, I'm <strong>Tang Zhantong</strong>. I'm a master's student at <strong>Southeast University</strong> (School of Medicine), working on <em>in vitro</em> models that replace animal experiments in respiratory disease research.</p>
        <p>I like cats, coding, and the overlap between biology and AI. I'm currently doing my PhD training at Guangzhou Laboratory.</p>
        <div class="about-links">
            <a href="mailto:zhantongtang@gmail.com">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
                Email
            </a>
            <a href="https://orcid.org/0009-0007-8038-7506" target="_blank">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S16.628 0 12 0zm-4.615 17.423h-2.174V9h2.174v8.423zm-1.087-9.56c-.668 0-1.21-.542-1.21-1.21 0-.669.542-1.21 1.21-1.21.668 0 1.21.541 1.21 1.21 0 .668-.542 1.21-1.21 1.21zm10.74 5.337c0 2.658-2.035 3.328-3.793 3.328-1.458 0-2.502-.497-2.906-.856v.614h-2.012V9h2.012v1.076c.404-.497 1.428-1.125 2.886-1.125 2.227 0 3.813 1.636 3.813 4.249zm-2.003-.024c0-1.49-.932-2.399-2.05-2.399-1.018 0-1.76.694-1.76 2.378 0 1.554.743 2.399 1.801 2.399 1.2 0 2.009-.974 2.009-2.378z"/></svg>
                ORCID
            </a>
            <a href="https://scholar.google.com/citations?user=f59aEisAAAAJ&hl=en" target="_blank">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"/></svg>
                Google Scholar
            </a>
            <a href="https://www.researchgate.net/profile/Tang-Zhantong" target="_blank">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M19.586 0c-2.123 0-4.152 1.153-5.09 3.017-.938-1.864-2.967-3.017-5.09-3.017C4.276 0 0 4.276 0 9.407c0 5.13 4.276 9.406 9.407 9.406.562 0 1.112-.05 1.648-.147l.82 2.67a.75.75 0 001.254.262l2.316-2.316c3.896-1.212 6.555-4.876 6.555-9.875C22 4.276 19.586 0 19.586 0zM6.61 13.263c-.718 0-1.3-.582-1.3-1.3 0-.718.582-1.3 1.3-1.3.719 0 1.3.582 1.3 1.3 0 .718-.581 1.3-1.3 1.3zm5.39 0c-.718 0-1.3-.582-1.3-1.3 0-.718.582-1.3 1.3-1.3.718 0 1.3.582 1.3 1.3 0 .718-.582 1.3-1.3 1.3z"/></svg>
                ResearchGate
            </a>
        </div>
    </div>
</div>

<!-- Research Highlights -->
<div class="highlights-section reveal">
    <h2 class="section-title">Research Interests</h2>
    <div class="highlights-grid">
        <div class="highlight-card reveal reveal-delay-1">
            <div class="highlight-icon">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#4a90e2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2v8"/>
                    <path d="M12 10c-2.5 0-5 2-6 5-.8 2.5-.5 5 1 6.5 1 1 2.5 1 3.5.5.8-.5 1.5-1.5 1.5-2.5V10"/>
                    <path d="M12 10c2.5 0 5 2 6 5 .8 2.5.5 5-1 6.5-1 1-2.5 1-3.5.5-.8-.5-1.5-1.5-1.5-2.5V10"/>
                </svg>
            </div>
            <h3>Respiratory Diseases</h3>
            <p>Building microfluidic models of influenza and other respiratory virus infections.</p>
        </div>
        <div class="highlight-card reveal reveal-delay-2">
            <div class="highlight-icon">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#4a90e2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="6" y="6" width="12" height="12" rx="2"/>
                    <path d="M6 10H3M6 14H3M18 10h3M18 14h3M10 6V3M14 6V3M10 18v3M14 18v3"/>
                    <rect x="9" y="9" width="6" height="6" rx="1"/>
                </svg>
            </div>
            <h3>Organ-on-a-Chip</h3>
            <p>Engineering organ-on-a-chip devices that replicate airway physiology for infection and drug studies.</p>
        </div>
        <div class="highlight-card reveal reveal-delay-3">
            <div class="highlight-icon">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#4a90e2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M9 3h6M9 3v7l-4 9a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1l-4-9V3"/>
                    <path d="M7 17h10"/>
                </svg>
            </div>
            <h3>In Vitro Modeling</h3>
            <p>Using ALI culture and 3D tissue engineering to build human airway models that replace animal experiments.</p>
        </div>
    </div>
</div>

<!-- Shared Resources -->
<div class="resources-section reveal">
    <div class="resources-grid">
        <div class="resource-panel">
            <h2 class="section-title">Recommended Reading</h2>
            <div class="resource-card reveal reveal-delay-1">
                <div class="resource-icon" aria-hidden="true">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#4a90e2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                        <path d="M8 7h8M8 11h6"/>
                    </svg>
                </div>
                <div class="resource-content">
                    <h3>Getting Started with Immunology</h3>
                    <p>If you are interested in learning immunology, I recommend <span class="resource-book-title">Cellular and Molecular Immunology, 8th Edition</span>.</p>
                </div>
            </div>
        </div>

        <div class="resource-panel">
            <div class="resource-heading">
                <h2 class="section-title">This Week's Research Picks</h2>
                <a class="resource-archive-link" href="/research-picks/">Archive</a>
            </div>
            <div class="github-picks">
                <a class="github-pick reveal reveal-delay-1" href="https://github.com/bowang-lab/scGPT" target="_blank" rel="noopener noreferrer">
                    <div class="github-pick-header">
                        <span class="github-pick-name">scGPT</span>
                        <span class="github-pick-stars">★ 1.6k</span>
                    </div>
                    <p>A foundation-model codebase for single-cell multi-omics, useful for annotation, perturbation, and representation learning.</p>
                </a>
                <a class="github-pick reveal reveal-delay-2" href="https://github.com/scverse/squidpy" target="_blank" rel="noopener noreferrer">
                    <div class="github-pick-header">
                        <span class="github-pick-name">Squidpy</span>
                        <span class="github-pick-stars">★ 581</span>
                    </div>
                    <p>Spatial single-cell analysis in Python, covering tissue-neighborhood graphs, spatial statistics, and image features.</p>
                </a>
                <a class="github-pick reveal reveal-delay-3" href="https://github.com/scverse/cellrank" target="_blank" rel="noopener noreferrer">
                    <div class="github-pick-header">
                        <span class="github-pick-name">CellRank</span>
                        <span class="github-pick-stars">★ 454</span>
                    </div>
                    <p>Fate mapping for multi-view single-cell data with Markov models, RNA velocity, and driver-gene analysis.</p>
                </a>
            </div>
        </div>
    </div>
</div>

<!-- NEWS -->
<div class="content-container reveal">
    <h2 class="section-title">NEWS</h2>
    
    <ul class="news-list">
        <li class="news-item">
            <span class="news-date">2026-07-15</span>
            <span class="news-content">
                An interesting read in Cell this week: a garlic compound cuts down mating and egg-laying in fruit flies and mosquitoes, which could point toward a new angle for controlling disease-carrying insects (<a href="https://doi.org/10.1016/j.cell.2026.03.037" target="_blank">DOI: 10.1016/j.cell.2026.03.037</a>).
            </span>
        </li>

        <li class="news-item">
            <span class="news-date">2026-07-02</span>
            <span class="news-content">
                Tang Zhantong attended the master's graduation ceremony at Southeast University, marking the official end of his work there. Remembering Southeast University, and remembering Nanjing.
                <a href="/assets/images/seu_master_graduation_2026.jpg" target="_blank">
                    <img src="/assets/images/seu_master_graduation_2026.jpg" alt="Tang Zhantong at Southeast University master's graduation ceremony" loading="lazy" style="display:block;max-width:100%;width:520px;margin-top:12px;border:1px solid var(--color-border-light);border-radius:6px;">
                </a>
            </span>
        </li>

        <li class="news-item">
            <span class="news-date">2026-05-22</span>
            <span class="news-content">
                Tang Zhantong passed his master's thesis oral defense at Southeast University with an Excellent grade. Congratulations!
                <a href="/assets/images/master_defense_2026.jpg" target="_blank">
                    <img src="/assets/images/master_defense_2026.jpg" alt="Master's thesis defense group photo" loading="lazy" style="display:block;max-width:100%;width:520px;margin-top:12px;border:1px solid var(--color-border-light);border-radius:6px;">
                </a>
            </span>
        </li>

        <li class="news-item">
            <span class="news-date">2026-05-09</span>
            <span class="news-content">Tang Zhantong will wrap up his work at Southeast University and move to Guangzhou Laboratory in July 2026 to begin the next chapter of research.</span>
        </li>

        <li class="news-item">
            <span class="news-date">2026-05-06</span>
            <span class="news-content">
                Tang Zhantong has been admitted to the joint PhD program of Guangzhou Laboratory and Sun Yat-sen University. Wishing all the best for what comes next!
                <a href="/assets/images/phd_admission_2026.png" target="_blank">
                    <img src="/assets/images/phd_admission_2026.png" alt="PhD admission list" loading="lazy" style="display:block;max-width:100%;width:520px;margin-top:12px;border:1px solid var(--color-border-light);border-radius:6px;">
                </a>
            </span>
        </li>

        <li class="news-item">
            <span class="news-date">2026-04-24</span>
            <span class="news-content">
                Tang Zhantong passed the master's thesis blind review at Southeast University with two A grades and advances to the oral defense. Best of luck!
                <a href="/assets/images/thesis_blind_review_2026.png" target="_blank">
                    <img src="/assets/images/thesis_blind_review_2026.png" alt="Thesis blind review results" loading="lazy" style="display:block;max-width:100%;width:520px;margin-top:12px;border:1px solid var(--color-border-light);border-radius:6px;">
                </a>
            </span>
        </li>

        <li class="news-item">
            <span class="news-date">2026-02-16</span>
            <span class="news-content">On February 16, 2026, we celebrated Chinese New Year in Xianyang, Shaanxi. Happy New Year!</span>
        </li>

        <li class="news-item">
            <span class="news-date">2026-01-06</span>
            <span class="news-content">Tang Zhantong will participate in the pre-defense for graduation from the Department of Genetics and Developmental Biology on Jan 7.</span>
        </li>
        
        <li class="news-item">
            <span class="news-date">2026-01-05</span>
            <span class="news-content">Tang Zhantong will go to Guangdong on Jan 14 for the joint PhD interview of Guangzhou Laboratory and Sun Yat-sen University. Best of luck!</span>
        </li>

        <li class="news-item">
            <span class="news-date">2026-01-05</span>
            <span class="news-content">My personal website is officially online!</span>
        </li>

        <li class="news-item">
            <span class="news-date">2025-12-31</span>
            <span class="news-content">Zhantong and Haoyu spent a pleasant New Year holiday in Qingdao, Shandong. Wishing everyone peace and health in the coming year!</span>
        </li>

        <li class="news-item">
            <span class="news-date">2025-12-27</span>
            <span class="news-content">Tang Zhantong attended the two-day doctoral interview at Sun Yat-sen University in Shenzhen.</span>
        </li>
    </ul>
</div>
