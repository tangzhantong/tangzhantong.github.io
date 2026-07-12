---
layout: default
title: News
lang: en
permalink: /news/
header_style: white
---

<style>
/* Header Styling for News Page */
header.site-header {
    position: absolute !important;
    top: 0;
    left: 0;
    width: 100%;
    background-color: transparent !important;
    border-bottom: none !important;
    z-index: 1000;
}

.news-page-container {
    position: relative;
    min-height: 100vh;
    width: 100%;
    /* Extend to top to be behind header */
    margin-top: -60px; 
    padding-top: 160px; /* More padding to account for header */
    /* Background Image */
    background: #1a1a2e;
}

/* Semi-transparent overlay to make text readable */
.news-overlay {
    background-color: rgba(255, 255, 255, 0.9);
    max-width: 800px;
    margin: 0 auto;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.news-list-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
    border-bottom: 1px solid #eee;
    font-size: 1.2rem;
    cursor: pointer;
    transition: background-color 0.2s;
}

.news-list-item:hover {
    background-color: rgba(0,0,0,0.02);
}

.news-list-item a {
    display: flex;
    width: 100%;
    text-decoration: none;
    color: inherit;
    align-items: center;
}

.news-date {
    font-weight: bold;
    color: #555;
    margin-right: 30px;
    min-width: 120px;
}

.news-title {
    color: #333;
    font-weight: 500;
}
</style>

<div class="news-page-container">
    <video autoplay muted loop playsinline style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;z-index:0;" poster="/assets/video/bg_poster.jpg" preload="none"><source src="/assets/video/bg.mp4" type="video/mp4"></video>
    <div class="news-overlay" style="position:relative;z-index:1;">
        <h1 style="text-align: center; margin-bottom: 40px;">News</h1>
        <div class="news-list-item">
            <a href="/nanjing-2026/">
                <span class="news-date">2026-07-10</span>
                <span class="news-title">My Beloved Nanjing</span>
            </a>
        </div>
        <div class="news-list-item">
            <a href="/cny-2026/">
                <span class="news-date">2026-02-16</span>
                <span class="news-title">Celebrating Chinese New Year</span>
            </a>
        </div>
        <div class="news-list-item">
            <a href="/greeting-2026/">
                <span class="news-date">2026-02-03</span>
                <span class="news-title">2026 Greeting</span>
            </a>
        </div>
    </div>
</div>
