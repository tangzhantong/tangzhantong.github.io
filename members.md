---
layout: default
title: "Team"
permalink: /members/
---

<style>
/* 导航栏透明化 */
header.site-header {
    position: absolute !important;
    top: 0; left: 0; width: 100%;
    background-color: transparent !important; border-bottom: none !important; z-index: 1000;
}
.site-title, .site-title:visited, .site-nav .page-link { color: #ffffff !important; text-shadow: 0 1px 3px rgba(0,0,0,0.5); }
.site-nav .menu-icon svg path { fill: #ffffff !important; }

/* Hero Banner */
.hero-wrapper {
    position: relative; width: 100vw; left: 50%; right: 50%;
    margin-left: -50vw; margin-right: -50vw; margin-top: -60px; margin-bottom: 60px;
}
.hero-banner {
    width: 100%; height: 400px;
    background-image: url('/assets/images/banner2.jpg'); /* 建议：换一张合影或校园风景 */
    background-size: cover; background-position: center;
    position: relative; display: flex; justify-content: center; align-items: center; color: white;
}
.hero-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); }
.hero-title { position: relative; z-index: 2; font-size: 3rem; font-weight: 700; letter-spacing: 2px; }

/* 成员内容 */
.intro-text { text-align: center; margin-bottom: 50px; color: #666; font-style: italic; font-size: 16px; max-width: 800px; margin: 0 auto 50px auto; }
.member-container { display: flex; flex-wrap: wrap; gap: 50px; justify-content: center; }
.member-card { text-align: center; width: 240px; }
.member-img { width: 160px; height: 160px; border-radius: 50%; object-fit: cover; border: 4px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
.member-name { margin-top: 20px; margin-bottom: 8px; font-size: 1.4rem; color: #333; }
.member-info { font-size: 14px; color: #555; line-height: 1.7; text-align: left; padding-left: 10px; }

footer, .site-footer { display: none !important; }
</style>

<div class="hero-wrapper">
    <div class="hero-banner">
        <div class="hero-overlay"></div>
        <h1 class="hero-title">成员介绍</h1>
    </div>
</div>

<div class="intro-text">
    <p>🏳️‍🌈 秉持多元、平等与包容（DEI）理念，反对任何形式的歧视，尊重性别平等与多元性取向。</p>
</div>

<div class="member-container">

  <div class="member-card">
    <img src="/assets/images/tang_qingdao0126.jpg" alt="唐展通" class="member-img">
    <h3 class="member-name">唐展通</h3>
    <div class="member-info">
      <strong>研究方向：</strong>基础生物学<br>
      <strong>学校：</strong>东南大学<br>
      <strong>邮箱：</strong>zhantongtang@gmail.com<br>
      <strong>爱好：</strong>陪伴猫咪、烹饪
    </div>
  </div>

  <div class="member-card">
    <img src="/assets/images/memberhaoyu.jpg" alt="浩宇" class="member-img">
    <h3 class="member-name">浩宇</h3>
    <div class="member-info">
      <strong>研究方向：</strong>大气科学<br>
      <strong>学校：</strong>中国海洋大学<br>
      <strong>爱好：</strong>健身、陪伴猫咪、烹饪(?)
    </div>
  </div>

  <div class="member-card">
    <img src="/assets/images/memberdabao.jpg" alt="大宝" class="member-img">
    <h3 class="member-name">大宝</h3>
    <div class="member-info">
      <strong>职位：</strong>吉祥物<br>
      <strong>出生日期：</strong>2025年5月6日<br>
      <strong>性格：</strong>粘人，肚肚禁摸
    </div>
  </div>

  <div class="member-card">
    <img src="/assets/images/songrong_0126.jpg" alt="松茸" class="member-img">
    <h3 class="member-name">松茸</h3>
    <div class="member-info">
      <strong>职位：</strong>吉祥物<br>
      <strong>学校：</strong>中国海洋大学<br>
      <strong>性格：</strong>粘人(超级！)
    </div>
  </div>

</div>