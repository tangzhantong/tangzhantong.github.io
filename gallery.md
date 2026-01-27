---
layout: default
title: "Gallery"
permalink: /gallery/
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
.site-nav .menu-icon svg path {
    fill: #ffffff !important;
}

/* --- 2. Hero Banner 顶部大图 --- */
.hero-wrapper {
    position: relative;
    width: 100vw;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    margin-top: -60px; /* 抵消 default 布局的顶部间距 */
    margin-bottom: 60px;
}

.hero-banner {
    width: 100%;
    height: 400px;
    background-image: url('/assets/images/banner1.jpg'); /* 建议：换一张风景或显微摄影大图 */
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
    background: rgba(0, 0, 0, 0.4); 
}

.hero-title {
    position: relative;
    z-index: 2;
    font-size: 3rem;
    font-weight: 700;
    letter-spacing: 2px;
    font-family: "Helvetica Neue", sans-serif;
}

/* --- 3. Gallery 卡片样式 (极简、直角、学术风) --- */
.gallery-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    max-width: 1200px;
    margin: 0 auto 60px auto;
}

.gallery-card {
    width: 350px; /* 稍微加宽，适合展示摄影作品 */
    background: #fff;
    border: 1px solid #eaeaea; /* 极细的灰色边框 */
    border-radius: 0; /* 【关键】直角，拒绝圆角 */
    padding-bottom: 15px;
    transition: all 0.3s ease;
}

.gallery-card:hover {
    border-color: #999; /* 悬停时边框加深 */
    transform: translateY(-2px); /* 极其微小的上浮 */
}

.gallery-img {
    width: 100%;
    height: 240px; /* 统一高度 */
    object-fit: cover;
    display: block;
    border-radius: 0; /* 直角 */
    filter: grayscale(20%); /* 默认加一点点灰度，显得更高级 */
    transition: filter 0.3s;
}

.gallery-card:hover .gallery-img {
    filter: grayscale(0%); /* 悬停恢复全彩 */
}

.gallery-info {
    padding: 15px 15px 0 15px;
}

.gallery-title {
    margin: 0 0 6px 0;
    font-size: 16px;
    font-weight: 600;
    color: #222;
    font-family: "Helvetica Neue", sans-serif;
}

.gallery-desc {
    font-size: 13px;
    color: #666;
    line-height: 1.6;
    margin: 0;
    font-family: sans-serif;
}

/* 隐藏系统默认页脚 */
footer, .site-footer {
    display: none !important;
}
</style>

<div class="hero-wrapper">
    <div class="hero-banner">
        <div class="hero-overlay"></div>
        <h1 class="hero-title">Gallery</h1>
    </div>
</div>

<p style="text-align: center; color: #666; margin-bottom: 50px; font-family: serif; font-style: italic; font-size: 1.1rem;">
<br>
  <small style="font-size: 0.9rem;">Capturing moments in science and life.</small>
</p>

<div class="gallery-container">

  <div class="gallery-card">
    <img src="/assets/images/songrong_0126.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">回家～</h3>
      <p class="gallery-desc">
        2026年1月25日 | 松茸结束了近一个月的寄养生活，祝福。（有点长大了嘿嘿）
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/dabao_new_bed.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">新卧室 😌</h3>
      <p class="gallery-desc">
        2026年1月 | 北方有些寒冷，父母为大宝准备了新的小房子（踩奶ing）。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/pic_haoyu_cat.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">猫咖时光</h3>
      <p class="gallery-desc">
        2026年1月 | 我们每次出行基本都会去猫咖，cat是世界的小精灵。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/banner1.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">青岛海底世界</h3>
      <p class="gallery-desc">
        2026年1月 | 新年伊始，我和浩宇参观了青岛海底世界。我很喜欢大海。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/dabao_sleep.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">Sleep 😴</h3>
      <p class="gallery-desc">
        2025年8月 | 大宝：别被我发现了！
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/dabao_home.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">新的家 👋</h3>
      <p class="gallery-desc">
        2025年1月 | 大宝刚到家，对一切都充满好奇。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/dabao_go_gome.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">回家～</h3>
      <p class="gallery-desc">
        2025年1月 | 由于我工作变动，不能陪伴大宝。我父母建议寄回家，于是在回家途中我拍下一张，心疼 🥹。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/banner2.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">玄武湖游玩</h3>
      <p class="gallery-desc">
        2025年4月 | 处在樱花季的南京很美（樱花季在清明节前后，可别错过！）。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/banner4.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">莫干山民宿</h3>
      <p class="gallery-desc">
        2024年4月 | 在莫干山游玩，民宿中的小温暖。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/sister_rabbit.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">小兔子</h3>
      <p class="gallery-desc">
        2024年某月 | 师姐将兔子带来实验室，很乖巧，我们都很喜欢！
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/cell_exp.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">细胞实验中...</h3>
      <p class="gallery-desc">
        2024年9月 | 经过6个月的基础实验，我终于开始细胞实验了，很激动也很小心翼翼。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/baby_dabao.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">Baby 大宝</h3>
      <p class="gallery-desc">
        2024年6月 | 我领养了大宝。是否觉得和未来的毛色有不同呢？
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/lab_western.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">Western Blot</h3>
      <p class="gallery-desc">
        2024年某月 | 蛋白成功从 Gel 转到 Membrane 上让我很有成就感。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/lab_cat.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">Lab Cat (Mom)</h3>
      <p class="gallery-desc">
        在生命健康高等研究院学习之初遇到的猫妈妈，治愈我那段时光。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/lab_babycat.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">Lab Cat (Kitten)</h3>
      <p class="gallery-desc">
        猫妈妈的孩子，直到和妈妈一起被送往救助站，祝愿幸福！
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/seu.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">东南大学大礼堂</h3>
      <p class="gallery-desc">
        2024年某月 | 四牌楼校区标志性建筑。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/autumn.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">东大秋景</h3>
      <p class="gallery-desc">
        2024年某月 | 东南大学四牌楼校区秋景。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/sunny.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">东大春景</h3>
      <p class="gallery-desc">
        2024年某月 | 东南大学四牌楼校区春景。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/shiyigong.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">施一公教授讲座</h3>
      <p class="gallery-desc">
        2024年1月 | 我很幸运抢到了施一公教授的讲座，即便是在九龙湖校区。我对生物学充满兴趣！
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/seu_sipailou_campus_snow.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">东大雪景</h3>
      <p class="gallery-desc">
        2023年12月 | 南京下雪，美丽的四牌楼。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/seu_sipailou_campus_doudou.jpg" class="gallery-img" alt="Photo">
    <div class="gallery-info">
      <h3 class="gallery-title">兜兜</h3>
      <p class="gallery-desc">
        四牌楼校区的顶流-兜兜，目前已经被领养，祝福！
      </p>
    </div>
  </div>

</div>