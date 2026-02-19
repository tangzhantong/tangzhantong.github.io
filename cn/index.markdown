---
layout: default
title: Home
lang: cn
permalink: /cn/
header_style: white
description: "唐展通的个人网站 - 致力于减少对实验动物的依赖和伤害，通过创新体外模型推动生物医学研究。"
---

<style>
/* --- 首页专用样式 --- */
.content-container {
    max-width: 900px;
    margin: 60px auto;
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

.news-list { list-style: none; padding: 0; margin: 0; }

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

.news-content { color: #444; }

/* About Me */
.about-section {
    max-width: 900px;
    margin: 80px auto 60px;
    padding: 0 20px;
    display: flex;
    gap: 40px;
    align-items: center;
}

.about-photo img {
    width: 180px;
    height: 180px;
    border-radius: 12px;
    object-fit: cover;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.about-text h2 { font-size: 1.6rem; margin-bottom: 12px; color: #333; }
.about-text p { font-size: 15px; line-height: 1.8; color: #555; margin-bottom: 10px; }

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

/* Research Highlights */
.highlights-section {
    max-width: 900px;
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

.highlight-icon { font-size: 2rem; margin-bottom: 12px; }
.highlight-card h3 { font-size: 1rem; margin-bottom: 8px; color: #333; }
.highlight-card p { font-size: 13px; color: #666; line-height: 1.6; }

@media (max-width: 768px) {
    .about-section { flex-direction: column; text-align: center; }
    .about-links { justify-content: center; }
}
</style>

<div class="video-container">
    <video autoplay muted loop playsinline id="bg-video" poster="/assets/video/bg_poster.jpg" preload="none">
        <source src="/assets/video/bg.mp4" type="video/mp4">
        Your browser does not support HTML5 video.
    </video>
    <div class="video-overlay"></div>
    <div class="video-content">
        <h1 class="hero-title">致力于减少对实验动物的依赖和伤害！</h1>
        <p class="hero-subtitle">Committed to reducing dependence on and harm to experimental animals!</p>
    </div>
</div>

<!-- 关于我 -->
<div class="about-section reveal">
    <div class="about-photo">
        <img src="/assets/images/memberzhantong.jpg" alt="唐展通个人照片" loading="lazy">
    </div>
    <div class="about-text">
        <h2>关于我</h2>
        <p>你好！我是<strong>唐展通</strong>，<strong>东南大学</strong>医学院硕士研究生，热爱生物学与生物医学工程。我的研究方向聚焦于构建<em>体外</em>模型，以减少对实验动物的依赖。</p>
        <p>我喜欢猫、编程、人工智能，以及探索生物学与工程学和AI的交叉领域。我将于2026年6月从东南大学毕业，并随即前往广州实验室开展我的博士训练。</p>
        <div class="about-links">
            <a href="https://x.com/Newkotang" target="_blank">𝕏 推特</a>
            <a href="https://orcid.org/0009-0007-8038-7506" target="_blank">🔬 ORCID</a>
            <a href="https://www.youtube.com/@Newko-t2v" target="_blank">▶ YouTube</a>
            <a href="https://www.instagram.com/jetb.rainslicensecrack/" target="_blank">📸 Instagram</a>
            <a href="https://scholar.google.com/citations?user=f59aEisAAAAJ&hl=en" target="_blank">🎓 谷歌学术</a>
            <a href="https://www.researchgate.net/profile/Tang-Zhantong" target="_blank">ʀɢ ResearchGate</a>
            <a href="https://space.bilibili.com/277751628" target="_blank">📺 Bilibili</a>
            <a href="mailto:zhantongtang@gmail.com">✉ 邮箱</a>
        </div>
    </div>
</div>

<!-- 研究方向 -->
<div class="highlights-section reveal">
    <h2 class="section-title">研究方向</h2>
    <div class="highlights-grid">
        <div class="highlight-card hover-lift">
            <div class="highlight-icon">🫁</div>
            <h3>呼吸系统疾病</h3>
            <p>利用先进的体外平台，模拟流感及呼吸道病毒感染过程。</p>
        </div>
        <div class="highlight-card hover-lift">
            <div class="highlight-icon">🧫</div>
            <h3>器官芯片</h3>
            <p>开发微流控芯片系统，模拟器官级别的生理功能与免疫应答。</p>
        </div>
        <div class="highlight-card hover-lift">
            <div class="highlight-icon">🔬</div>
            <h3>体外建模</h3>
            <p>构建生理相关的细胞培养体系，作为动物实验的替代方案。</p>
        </div>
    </div>
</div>

<!-- 最新动态 -->
<div class="content-container reveal">
    <h2 class="section-title">最新动态</h2>
    
    <ul class="news-list">
        <li class="news-item">
            <span class="news-date">2026-02-16</span>
            <span class="news-content">2026年2月16日，我们在陕西省咸阳市庆祝中国新年。祝愿新年快乐！</span>
        </li>

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
