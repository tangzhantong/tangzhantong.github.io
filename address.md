---
layout: default
title: "Contact"
lang: en
permalink: /address/
header_style: white
description: "Contact Tang Zhantong — Guangzhou Laboratory and Sun Yat-sen University Shenzhen Campus."
---

<style>
/* === Contact 页面专用样式 === */
.contact-container {
    max-width: 900px;
    margin: 0 auto 80px auto;
    padding: 0 20px;
    text-align: center;
}

.info-group { margin-bottom: 50px; }

.info-label {
    font-size: 12px;
    font-weight: 700;
    color: #999;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
    display: block;
}

.info-value {
    font-size: 20px;
    color: #333;
    font-weight: 400;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    line-height: 1.6;
}

.info-sub {
    font-size: 14px;
    color: #666;
    margin-top: 5px;
}

.mail-link {
    color: #333;
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: border-color 0.3s;
}

.mail-link:hover { border-bottom: 1px solid #333; }

.map-wrapper {
    width: 100%;
    height: 400px;
    background: #f0f0f0;
}

.map-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
}

.map-cell {
    position: relative;
    height: 400px;
    background: #f0f0f0;
}

.map-cell iframe {
    width: 100%;
    height: 100%;
    border: 0;
    filter: grayscale(10%);
}

.map-cell .map-caption {
    position: absolute;
    left: 12px;
    bottom: 12px;
    background: rgba(255,255,255,0.92);
    color: #333;
    font-size: 13px;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 4px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.locations-grid {
    display: flex;
    justify-content: center;
    gap: 60px;
    flex-wrap: wrap;
    margin-bottom: 50px;
}

.locations-grid .info-group {
    margin-bottom: 0;
    max-width: 360px;
}

@media (max-width: 768px) {
    .map-grid { grid-template-columns: 1fr; }
}
</style>

<div class="hero-wrapper">
    <div class="hero-banner" style="background: #1a1a2e; overflow: hidden;">
        <video autoplay muted loop playsinline style="position:absolute;top:50%;left:50%;min-width:100%;min-height:100%;transform:translate(-50%,-50%);object-fit:cover;" poster="/assets/video/bg_poster.jpg" preload="none"><source src="/assets/video/bg.mp4" type="video/mp4"></video>
        <div class="hero-overlay"></div>
        <h1 class="hero-title">Contact</h1>
    </div>
</div>

<div class="contact-container reveal">
    
    <div class="locations-grid">

        <div class="info-group">
            <span class="info-label">Address 1</span>
            <div class="info-value">Guangzhou Laboratory</div>
            <div class="info-sub">International Bio Island, Guangzhou, Guangdong Province</div>
        </div>

        <div class="info-group">
            <span class="info-label">Address 2</span>
            <div class="info-value">Medical Park, Shenzhen Campus, Sun Yat-sen University</div>
            <div class="info-sub">Guangming District, Shenzhen, Guangdong Province</div>
        </div>

    </div>

    <div style="display: flex; justify-content: center; gap: 60px; flex-wrap: wrap;">

        <div class="info-group">
            <span class="info-label">Email</span>
            <div class="info-value">
                <a href="mailto:zhantongtang@gmail.com" class="mail-link">zhantongtang@gmail.com</a>
            </div>
        </div>

        <div class="info-group">
            <span class="info-label">Phone</span>
            <div class="info-value">187 0042 2328</div>
        </div>

    </div>

</div>

<div class="map-grid">
    <div class="map-cell">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d8446.647904020454!2d113.36318373264822!3d23.06286168886883!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x34025539c19fbb1b%3A0x931754be65b3f5fa!2z5bm_5bee5Zu96ZmF55Sf54mp5bKb!5e1!3m2!1sen!2sus!4v1778382050367!5m2!1sen!2sus" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        <span class="map-caption">Guangzhou Laboratory</span>
    </div>
    <div class="map-cell">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7321.680499534268!2d113.94812447686517!3d22.799700359562767!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x34038ff0a75e6055%3A0xed731d3b76eb38f2!2sSYSU%20Academic%20Vila%2CShenzhen%20Campus!5e1!3m2!1sen!2sus!4v1778382266276!5m2!1sen!2sus" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        <span class="map-caption">SYSU Shenzhen — Medical Park</span>
    </div>
</div>