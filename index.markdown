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

/* --- 2. 全屏轮播 Hero Section --- */

.slider-container {
    position: relative;
    width: 100vw;
    height: 100vh; /* 全屏高度 */
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    margin-top: -60px; /* 抵消顶部间距 */
    overflow: hidden;
}

.slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    opacity: 0;
    transition: opacity 1.5s ease-in-out; /* 淡入淡出效果 */
    z-index: 1;
}

.slide.active {
    opacity: 1;
    z-index: 2;
}

/* 遮罩层 */
.slider-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.3); /* 30% 黑色遮罩 */
    z-index: 3;
    pointer-events: none; /* 让点击穿透 */
}

/* 标题内容 */
.slider-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 4;
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

/* 切换按钮 */
.slider-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0,0,0,0.2);
    color: white;
    border: none;
    font-size: 2rem;
    padding: 15px;
    cursor: pointer;
    z-index: 5;
    transition: background 0.3s;
    border-radius: 5px;
}

.slider-btn:hover {
    background: rgba(0,0,0,0.5);
}

.prev-btn { left: 20px; }
.next-btn { right: 20px; }

/* 移动端适配 */
@media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .slider-btn { padding: 10px; font-size: 1.5rem; }
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

<div class="slider-container">
    <div class="slide active" style="background-image: url('/assets/images/home_bg_1.jpg');"></div>
    <div class="slide" style="background-image: url('/assets/images/home_bg_2.jpg');"></div>
    <div class="slide" style="background-image: url('/assets/images/home_bg_3.jpg');"></div>
    <div class="slide" style="background-image: url('/assets/images/home_bg_4.jpg');"></div>
    
    <div class="slider-overlay"></div>
    
    <div class="slider-content">
        <h1 class="hero-title">致力于减少对实验动物的依赖和伤害！</h1>
    </div>

    <button class="slider-btn prev-btn" onclick="changeSlide(-1)">&#10094;</button>
    <button class="slider-btn next-btn" onclick="changeSlide(1)">&#10095;</button>
</div>

<script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;

    function changeSlide(direction) {
        // 移除当前 active
        slides[currentSlide].classList.remove('active');
        
        // 计算新索引
        currentSlide += direction;
        
        // 循环逻辑
        if (currentSlide >= totalSlides) {
            currentSlide = 0;
        } else if (currentSlide < 0) {
            currentSlide = totalSlides - 1;
        }
        
        // 添加新 active
        slides[currentSlide].classList.add('active');
    }

    // 自动播放 (每 5 秒切换)
    setInterval(() => {
        changeSlide(1);
    }, 5000);
</script>

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