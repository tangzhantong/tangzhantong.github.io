---
layout: default
title: "Research"
permalink: /research/
---

<style>
/* --- 1. 导航栏透明化 (沉浸式效果) --- */
header.site-header {
    position: absolute !important;
    top: 0;
    left: 0;
    width: 100%;
    background-color: transparent !important;
    border-bottom: none !important;
    z-index: 1000;
}
.site-title, .site-title:visited, .site-nav .page-link {
    color: #ffffff !important;
    text-shadow: 0 1px 3px rgba(0,0,0,0.5);
}
.site-nav .menu-icon svg path { fill: #ffffff !important; }

/* --- 2. Hero Banner --- */
.hero-wrapper {
    position: relative;
    width: 100vw;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    margin-top: -60px; /* 抵消顶部间距 */
    margin-bottom: 60px;
}
.hero-banner {
    width: 100%;
    height: 450px;
    background-image: url('/assets/images/research_bg.jpg');
    background-size: cover;
    background-position: center;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
}
.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5); 
}
.hero-content {
    position: relative;
    z-index: 2;
    text-align: center;
    padding: 0 20px;
}
.hero-title {
    font-size: 3.5rem;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 15px;
    font-family: "Helvetica Neue", Arial, sans-serif;
}
.hero-subtitle {
    font-size: 1.1rem;
    font-weight: 300;
    letter-spacing: 1px;
    border-top: 1px solid rgba(255,255,255,0.6);
    padding-top: 15px;
    display: inline-block;
}

/* --- 3. 正文样式 --- */
.content-section {
    max-width: 900px;
    margin: 0 auto 60px auto;
    padding: 0 20px;
}
.project-card {
    margin-bottom: 50px;
    border-bottom: 1px solid #eee;
    padding-bottom: 40px;
}
.project-title {
    font-size: 1.8rem;
    color: #333;
    margin-bottom: 20px;
    border-left: 5px solid #4a90e2; /* 学术蓝 */
    padding-left: 15px;
    line-height: 1.3;
}
.project-desc {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #444;
    text-align: justify;
}
.placeholder-text {
    color: #999;
    font-style: italic;
    font-size: 0.9rem;
    margin-top: 10px;
    display: block;
}
/* 隐藏默认 Footer */
footer, .site-footer { display: none !important; }
</style>

<div class="hero-wrapper">
    <div class="hero-banner">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1 class="hero-title">研究内容</h1>
            <div class="hero-subtitle">
                研究领域：呼吸系统疾病；体外模拟；器官芯片；免疫学；病毒学
            </div>
        </div>
    </div>
</div>

<div class="content-section">
    <div class="project-card">
        <h2 class="project-title">1. 器官芯片体外模拟流感免疫应答</h2>
        <div class="project-desc">
            <p>
                本课题旨在探索在器官芯片中，模拟流感病毒感染后机体的免疫应答
            </p>
            <span class="placeholder-text">(敬请期待...)</span>
        </div>
    </div>
    

</div>