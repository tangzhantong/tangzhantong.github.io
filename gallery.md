---
layout: page
title: "📷 Gallery"
permalink: /gallery/
---

<style>
  .gallery-container {
    display: flex;
    flex-wrap: wrap;
    gap: 30px; /* 卡片之间的间距 */
    justify-content: center; /* 居中对齐 */
  }
  
  .gallery-card {
    width: 300px; /* 每个卡片的宽度 */
    background: #fff;
    border: 1px solid #eee;
    border-radius: 8px; /* 圆角 */
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05); /* 淡淡的阴影 */
    transition: transform 0.2s; /* 动画效果 */
  }
  
  .gallery-card:hover {
    transform: translateY(-5px); /* 鼠标悬停时上浮 */
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  }

  .gallery-img {
    width: 100%;
    height: 200px; /* 图片高度统一，防止参差不齐 */
    object-fit: cover; /* 保证图片填满且不变形 */
    display: block;
  }

  .gallery-info {
    padding: 15px;
  }

  .gallery-title {
    margin: 0 0 8px 0;
    font-size: 16px;
    font-weight: bold;
    color: #333;
  }

  .gallery-desc {
    font-size: 14px;
    color: #666;
    line-height: 1.5;
    margin: 0;
  }
</style>

<p style="text-align: center; color: #666; margin-bottom: 40px;">
  记录生活的精彩瞬间与科研成果。<br>
  <small>Capturing moments in science and life.</small>
</p>

<div class="gallery-container">

  <div class="gallery-card">
    <img src="/assets/images/pic_haoyu_cat.jpg" class="gallery-img" alt="Conference">
    <div class="gallery-info">
      <h3 class="gallery-title">猫咖</h3>
      <p class="gallery-desc">
        2026年1月，我们每次出行基本都会去猫咖，cat是世界的小精灵。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/banner1.jpg" class="gallery-img" alt="Conference">
    <div class="gallery-info">
      <h3 class="gallery-title">青岛海底世界</h3>
      <p class="gallery-desc">
        2026年1月，新年伊始，我和浩宇参观了青岛海底世界。我很喜欢大海。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/dabao_sleep.jpg" class="gallery-img" alt="Conference">
    <div class="gallery-info">
      <h3 class="gallery-title">Sleep😴</h3>
      <p class="gallery-desc">
        2025年8月，大宝：别放我发现了！。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/dabao_home.jpg" class="gallery-img" alt="Conference">
    <div class="gallery-info">
      <h3 class="gallery-title">新的家👋</h3>
      <p class="gallery-desc">
        2025年1月，大宝刚到家，对一切的充满好奇。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/dabao_go_gome.jpg" class="gallery-img" alt="Conference">
    <div class="gallery-info">
      <h3 class="gallery-title">回家～</h3>
      <p class="gallery-desc">
        2025年1月，由于我工作变动，不能陪伴大宝。我父母建议寄回家，于是在回家途中我拍下一张，心疼🥹。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/banner2.jpg" class="gallery-img" alt="Team Building">
    <div class="gallery-info">
      <h3 class="gallery-title">玄武湖游玩</h3>
      <p class="gallery-desc">
        2025年4月，处在樱花季的南京很美（樱花季在清明节前后，可别错过！）。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/banner4.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">莫干山民宿</h3>
      <p class="gallery-desc">
        2024年4月，在莫干山游玩，民宿中的小温暖。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/sister_rabbit.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">小兔子</h3>
      <p class="gallery-desc">
        2024年某月，师姐将兔子带来实验室，很乖巧，我们都很喜欢！
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/cell_exp.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">细胞实验中。。。</h3>
      <p class="gallery-desc">
        2024年9月大概，经过6个月的基础实验，我终于开始细胞实验了，很激动也很小心翼翼。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/lab_western.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">western</h3>
      <p class="gallery-desc">
        2024年某月，我认为western中蛋白成功从gel到membrane上让我很有成就感。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/lab_cat.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">lab_cat</h3>
      <p class="gallery-desc">
        在生命健康高等研究院学习之初遇到的猫妈妈，治愈我那段时光。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/lab_babycat.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">lab_cat</h3>
      <p class="gallery-desc">
        猫妈妈的孩子，直到和妈妈一起被送往救助站，祝愿幸福！
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/seu.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">东南大学四牌楼校区大礼堂</h3>
      <p class="gallery-desc">
        2024年某月。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/autumn.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">东南大学四牌楼校区秋景</h3>
      <p class="gallery-desc">
        2024年某月。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/sunny.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">东南大学四牌楼校区春景</h3>
      <p class="gallery-desc">
        2024年某月。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/seu_sipailou_campus_snow.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">东南大学四牌楼校区雪景</h3>
      <p class="gallery-desc">
        2023年12月，南京下雪，美丽的四牌楼。
      </p>
    </div>
  </div>

  <div class="gallery-card">
    <img src="/assets/images/seu_sipailou_campus_doudou.jpg" class="gallery-img" alt="Research">
    <div class="gallery-info">
      <h3 class="gallery-title">兜兜</h3>
      <p class="gallery-desc">
        四牌楼校区的顶流-兜兜，目前已经被领养，祝福！
      </p>
    </div>
  </div>


</div>