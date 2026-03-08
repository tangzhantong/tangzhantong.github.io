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
    color: #333;
    margin-bottom: 50px;
    letter-spacing: -0.02em;
}

.news-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.news-item {
    display: flex;
    align-items: flex-start;
    padding: 20px 0;
    border-bottom: 1px solid #f0f0f0;
    font-size: 16px;
    line-height: 1.8;
}

.news-date {
    font-weight: 600;
    color: #888;
    min-width: 130px;
    margin-right: 30px;
    font-family: monospace;
}

.news-content {
    color: #444;
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
    border-radius: 12px;
    object-fit: cover;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.about-text h2 {
    font-size: 1.6rem;
    margin-bottom: 12px;
    color: #333;
    letter-spacing: -0.02em;
}

.about-text p {
    font-size: 15px;
    line-height: 1.8;
    color: #555;
    margin-bottom: 10px;
}

.about-links {
    display: flex;
    gap: 12px;
    margin-top: 15px;
    flex-wrap: wrap;
}

.about-links a {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border: 1px solid #ddd;
    border-radius: 20px;
    font-size: 13px;
    color: #555 !important;
    transition: all 0.3s;
}

.about-links a:hover {
    border-color: #333;
    color: #333 !important;
    transform: translateY(-1px);
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
    gap: 20px;
    margin-top: 30px;
}

.highlight-card {
    padding: 25px;
    border: 1px solid #eee;
    border-radius: 4px;
    transition: all 0.3s ease;
    text-align: center;
}

.highlight-card:hover {
    border-color: #999;
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}

.highlight-icon {
    display: flex;
    justify-content: center;
    margin-bottom: 16px;
}

.highlight-card h3 {
    font-size: 1rem;
    margin-bottom: 8px;
    color: #333;
}

.highlight-card p {
    font-size: 13px;
    color: #666;
    line-height: 1.6;
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
</div>

<!-- About Me -->
<div class="about-section reveal">
    <div class="about-photo">
        <img src="/assets/images/tang_selfish.png" alt="Tang Zhantong portrait" loading="lazy">
    </div>
    <div class="about-text">
        <h2>About Me</h2>
        <p>Hi! I'm <strong>Tang Zhantong</strong>, a master's student at <strong>Southeast University</strong> (School of Medicine), passionate about biology and biomedical engineering. My research focuses on building <em>in vitro</em> models to reduce dependence on experimental animals.</p>
        <p>I love cats, coding, artificial intelligence, and exploring the intersection of biology, engineering, and AI. I will graduate from Southeast University in June 2026 and immediately proceed to Guangzhou Laboratory to conduct my doctoral training.</p>
        <div class="about-links">
            <a href="mailto:zhantongtang@gmail.com">✉ Email</a>
            <a href="https://orcid.org/0009-0007-8038-7506" target="_blank">🔬 ORCID</a>
            <a href="https://scholar.google.com/citations?user=f59aEisAAAAJ&hl=en" target="_blank">🎓 Google Scholar</a>
            <a href="https://www.researchgate.net/profile/Tang-Zhantong" target="_blank">ʀɢ ResearchGate</a>
        </div>
    </div>
</div>

<!-- Research Highlights -->
<div class="highlights-section reveal">
    <h2 class="section-title">Research Interests</h2>
    <div class="highlights-grid">
        <div class="highlight-card hover-lift">
            <div class="highlight-icon">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#4a90e2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2v8"/>
                    <path d="M12 10c-2.5 0-5 2-6 5-.8 2.5-.5 5 1 6.5 1 1 2.5 1 3.5.5.8-.5 1.5-1.5 1.5-2.5V10"/>
                    <path d="M12 10c2.5 0 5 2 6 5 .8 2.5.5 5-1 6.5-1 1-2.5 1-3.5.5-.8-.5-1.5-1.5-1.5-2.5V10"/>
                </svg>
            </div>
            <h3>Respiratory Diseases</h3>
            <p>Modeling influenza and respiratory virus infections using advanced in vitro platforms.</p>
        </div>
        <div class="highlight-card hover-lift">
            <div class="highlight-icon">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#4a90e2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="6" y="6" width="12" height="12" rx="2"/>
                    <path d="M6 10H3M6 14H3M18 10h3M18 14h3M10 6V3M14 6V3M10 18v3M14 18v3"/>
                    <rect x="9" y="9" width="6" height="6" rx="1"/>
                </svg>
            </div>
            <h3>Organ-on-a-Chip</h3>
            <p>Developing microfluidic chip systems to simulate organ-level physiology and immune responses.</p>
        </div>
        <div class="highlight-card hover-lift">
            <div class="highlight-icon">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#4a90e2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M9 3h6M9 3v7l-4 9a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1l-4-9V3"/>
                    <path d="M7 17h10"/>
                </svg>
            </div>
            <h3>In Vitro Modeling</h3>
            <p>Creating physiologically relevant cell culture systems as alternatives to animal testing.</p>
        </div>
    </div>
</div>

<!-- NEWS -->
<div class="content-container reveal">
    <h2 class="section-title">NEWS</h2>
    
    <ul class="news-list">
        <li class="news-item">
            <span class="news-date">2026-02-16</span>
            <span class="news-content">On February 16, 2026, we celebrated Chinese New Year in Xianyang, Shaanxi. Happy New Year!</span>
        </li>

        <li class="news-item">
            <span class="news-date">2026-01-09</span>
            <span class="news-content">Tang Zhantong will attend the PhD entrance exam at the National Institute of Genetics / SOKENDAI, Japan on Jan 19-20. Best of luck!</span>
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