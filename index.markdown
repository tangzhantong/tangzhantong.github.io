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

/* 移动端 */
@media (max-width: 768px) {
    .about-section {
        flex-direction: column;
        text-align: center;
    }
    .about-links {
        justify-content: center;
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
        <p>Hi, I'm <strong>Tang Zhantong</strong>. I'm a PhD student in the joint program of <strong>Sun Yat-sen University</strong> and <strong>Guangzhou Laboratory</strong>, working on <em>in vitro</em> models that replace animal experiments in respiratory disease research.</p>
        <p>I like cats, coding, and the overlap between biology and AI. I did my master's at Southeast University (School of Medicine).</p>
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

<!-- NEWS -->
<div class="content-container reveal">
    <h2 class="section-title">NEWS</h2>
    
    <ul class="news-list">
        <li class="news-item">
            <span class="news-date">2026-07-15</span>
            <span class="news-content">
                An interesting read in Cell this week: a garlic compound cuts down mating and egg-laying in fruit flies and mosquitoes, which could point toward a new angle for controlling disease-carrying insects (<a href="https://doi.org/10.1016/j.cell.2026.03.037" target="_blank" style="color:#007398 !important;">DOI: 10.1016/j.cell.2026.03.037</a>).
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
