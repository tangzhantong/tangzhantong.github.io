---
layout: default
header_style: white
lang: en
---

<style>
/* --- 1. 核心魔法：改造导航栏 (仅在首页生效) --- */

/* 让 Header 绝对定位，覆盖在视频之上 */
header.site-header {
    position: absolute !important;
    top: 0;
    left: 0;
    width: 100%;
    background-color: transparent !important; /* 背景透明 */
    border-bottom: none !important; /* 去掉底部的线 */
    z-index: 1000; /* 保证它在视频上面 */
}

/* --- 2. 全屏视频背景 Hero Section --- */

.video-container {
    position: relative;
    width: 100vw;
    height: 100vh; /* 全屏高度 */
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    margin-top: -60px; /* 抵消顶部间距 */
    overflow: hidden;
    background-color: #1a1a2e; /* 深色占位背景 */
    background-image: url('/assets/video/bg_poster.jpg');
    background-size: cover;
    background-position: center;
}

#bg-video {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    z-index: 1;
    transform: translate(-50%, -50%);
    object-fit: cover; /* 保证充满屏幕 */
}

/* 遮罩层 */
.video-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.4); /* 40% 黑色遮罩，提高文字可读性 */
    z-index: 2;
    pointer-events: none; /* 让点击穿透 */
}

/* 标题内容 */
.video-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 3;
    text-align: center;
    width: 100%;
    padding: 0 20px;
    color: white;
}

.hero-title {
    font-size: 3.5rem;
    font-weight: 700;
    letter-spacing: 4px; 
    margin: 0;
    text-shadow: 0 4px 15px rgba(0,0,0,0.4);
    font-family: "Helvetica Neue", sans-serif;
}

/* 移动端适配 */
@media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
}

/* --- 3. NEWS 区域 (保持原样，优化间距) --- */
.content-container {
    max-width: 900px;
    margin: 60px auto; /* 上方留出距离 */
    padding: 0 20px;
}

.section-title {
    text-align: center;
    font-size: 1.8rem;
    font-weight: 700;
    color: #333;
    margin-bottom: 50px;
    letter-spacing: 2px;
    text-transform: uppercase;
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
    font-weight: 700;
    color: #d93025;
    min-width: 130px;
    margin-right: 30px;
    font-family: monospace; 
}

.news-content {
    color: #444;
}
</style>

<div class="video-container">
    <video autoplay muted loop playsinline id="bg-video" poster="/assets/video/bg_poster.jpg">
        <source src="/assets/video/bg.mp4" type="video/mp4">
        Your browser does not support HTML5 video.
    </video>
    
    <div class="video-overlay"></div>
    
    <div class="video-content">
        <h1 class="hero-title">Committed to reducing dependence on and harm to experimental animals!</h1>
    </div>
</div>

<div class="content-container">
    <h2 class="section-title">NEWS</h2>
    
    <ul class="news-list">
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