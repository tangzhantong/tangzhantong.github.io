---
layout: default
---

<style>
/* --- 1. 核心魔法：改造导航栏 (仅在首页生效) --- */

/* 让 Header 绝对定位，覆盖在图片之上 */
header.site-header {
    position: absolute !important;
    top: 0;
    left: 0;
    width: 100%;
    background-color: transparent !important; /* 背景透明 */
    border-bottom: none !important; /* 去掉底部的线 */
    z-index: 1000; /* 保证它在图片上面 */
}

/* 让导航栏里的文字变成白色 */
.site-title, 
.site-title:visited,
.site-nav .page-link {
    color: #ffffff !important;
    text-shadow: 0 1px 3px rgba(0,0,0,0.5); /* 加一点阴影，防止背景太亮时看不清文字 */
}

/* 如果有 SVG 图标（如汉堡菜单），也改成白色 */
.site-nav .menu-icon svg path {
    fill: #ffffff !important;
}

/* --- 2. 沉浸式 Hero Section (全屏大图) --- */

.hero-wrapper {
    position: relative;
    /* 强制突破父容器限制，实现全屏宽度 */
    width: 100vw;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    
    /* 关键：抵消掉原本 main 区域的内边距，让图片顶到浏览器最上沿 */
    margin-top: -60px; 
    padding-top: 0; 
}

.hero-banner {
    width: 100%;
    
    /* === 修改这里：从 100vh 改为 70vh (屏幕高度的 70%) === */
    height: 70vh; 
    min-height: 450px; /* 设置一个最小高度，防止在很扁的屏幕上显示不全内容 */
    
    /* 背景图设置 */
    background-image: url('/assets/images/banner1.jpg'); 
    background-size: cover;
    background-position: center;
    
    /* 布局 */
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

/* 遮罩层：稍微加深一点背景，确保白色文字清晰可见 */
.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.3); /* 30% 的黑色遮罩 */
}

.hero-content {
    position: relative;
    z-index: 2;
    text-align: center;
    color: white;
    padding: 0 20px;
    margin-top: 30px; /* 稍微调整，保证视觉平衡 */
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
    .hero-banner { height: 60vh; } /* 手机上可以稍微再小一点，比如 60% */
    .hero-wrapper { margin-top: -56px; } 
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

<div class="hero-wrapper">
    <div class="hero-banner">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1 class="hero-title">我的研究致力于通过器官芯片模型重建关键生理与病理过程，以减少对实验动物的依赖和伤害</h1>
        </div>
    </div>
</div>

<div class="content-container">
    <h2 class="section-title">NEWS</h2>
    
    <ul class="news-list">
        <li class="news-item">
            <span class="news-date">2026-01-09</span>
            <span class="news-content">唐展通将于1.19日，1.20日参加日本国立遗传学研究所/SOKENDAI遗传学课程的博士入学考试，祝一切顺利！</span>
        </li>
        
        <li class="news-item">
            <span class="news-date">2026-01-06</span>
            <span class="news-content">唐展通将于1.7日参加遗传与发育生物学系毕业预答辩。</span>
        </li>
        
        <li class="news-item">
            <span class="news-date">2026-01-05</span>
            <span class="news-content">唐展通将于1.14日前往广东参加广州国家实验室-中山大学联合培养博士面试，祝一切顺利！</span>
        </li>

        <li class="news-item">
            <span class="news-date">2026-01-05</span>
            <span class="news-content">我的个人网站正式上线了！</span>
        </li>

        <li class="news-item">
            <span class="news-date">2025-12-31</span>
            <span class="news-content">展通和浩宇在山东青岛度过了愉快的元旦假期。祝愿新的一年平安健康！</span>
        </li>

        <li class="news-item">
            <span class="news-date">2025-12-27</span>
            <span class="news-content">唐展通在深圳参加了中山大学博士面试，为期两天。</span>
        </li>
    </ul>
</div>