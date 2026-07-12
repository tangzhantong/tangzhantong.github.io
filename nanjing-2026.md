---
layout: default
title: My Beloved Nanjing
lang: en
permalink: /nanjing-2026/
header_style: white
---

<style>
.nanjing-page {
    max-width: 980px;
    margin: 100px auto;
    padding: 20px;
    font-family: "Helvetica Neue", Arial, "PingFang SC", "Microsoft YaHei", sans-serif;
}

.nanjing-title {
    font-size: 2.25rem;
    font-weight: 700;
    color: #333;
    margin-bottom: 10px;
    text-align: center;
}

.nanjing-date {
    display: block;
    text-align: center;
    color: #777;
    margin-bottom: 34px;
    font-style: italic;
}

.nanjing-content {
    max-width: 760px;
    margin: 0 auto 42px;
    font-size: 1.12rem;
    line-height: 1.9;
    color: #444;
    text-align: center;
}

.nanjing-carousel {
    position: relative;
}

.nanjing-track {
    display: flex;
    gap: 18px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    padding: 6px 2px 18px;
    scrollbar-width: thin;
}

.nanjing-slide {
    flex: 0 0 100%;
    scroll-snap-align: center;
    aspect-ratio: 4 / 3;
    background: #f5f5f7;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.nanjing-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    border-radius: 8px;
}

.nanjing-slide.is-portrait img {
    object-fit: contain;
    background: #f5f5f7;
}

.nanjing-control {
    position: absolute;
    top: 50%;
    width: 42px;
    height: 42px;
    border: none;
    border-radius: 50%;
    background: rgba(255,255,255,0.86);
    color: #333;
    font-size: 2rem;
    line-height: 1;
    cursor: pointer;
    transform: translateY(-50%);
    box-shadow: 0 4px 14px rgba(0,0,0,0.16);
}

.nanjing-control:hover {
    background: #fff;
}

.nanjing-prev {
    left: 14px;
}

.nanjing-next {
    right: 14px;
}

.nanjing-dots {
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 18px;
}

.nanjing-dot {
    width: 8px;
    height: 8px;
    border: 0;
    border-radius: 50%;
    background: #c7c7cc;
    cursor: pointer;
    padding: 0;
}

.nanjing-dot.active {
    background: #333;
}

.back-link {
    display: inline-block;
    margin-top: 44px;
    color: #666;
    text-decoration: none;
    border-bottom: 1px solid #ccc;
    transition: all 0.2s;
}

.back-link:hover {
    color: #333;
    border-color: #333;
}

@media (max-width: 768px) {
    .nanjing-page {
        margin: 80px auto;
        padding: 16px;
    }

    .nanjing-title {
        font-size: 1.9rem;
    }

    .nanjing-slide {
        flex-basis: 92%;
    }

    .nanjing-control {
        display: none;
    }
}
</style>

<div class="nanjing-page">
    <h1 class="nanjing-title">My Beloved Nanjing</h1>
    <span class="nanjing-date">2026-07-10</span>

    <div class="nanjing-content">
        <p>There are so many stories in my encounters with Nanjing. The warmth and familiarity of Nanjing are something no other city has given me. I hope to meet you again in the future!</p>
    </div>

    <div class="nanjing-carousel" aria-label="南京照片">
        <div class="nanjing-track">
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-01.jpg' | relative_url }}" alt="南京照片 1" loading="eager"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-02.jpg' | relative_url }}" alt="南京照片 2" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-03.jpg' | relative_url }}" alt="南京照片 3" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-04.jpg' | relative_url }}" alt="南京照片 4" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-05.jpg' | relative_url }}" alt="南京照片 5" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-06.jpg' | relative_url }}" alt="南京照片 6" loading="lazy"></div>
            <div class="nanjing-slide is-portrait"><img src="{{ '/assets/images/nanjing/nanjing-07.jpg' | relative_url }}" alt="南京照片 7" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-08.jpg' | relative_url }}" alt="南京照片 8" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-09.jpg' | relative_url }}" alt="南京照片 9" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-10.jpg' | relative_url }}" alt="南京照片 10" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-11.jpg' | relative_url }}" alt="南京照片 11" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-12.jpg' | relative_url }}" alt="南京照片 12" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-13.jpg' | relative_url }}" alt="南京照片 13" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-14.jpg' | relative_url }}" alt="南京照片 14" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-15.jpg' | relative_url }}" alt="南京照片 15" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-16.jpg' | relative_url }}" alt="南京照片 16" loading="lazy"></div>
            <div class="nanjing-slide is-portrait"><img src="{{ '/assets/images/nanjing/nanjing-17.jpg' | relative_url }}" alt="南京照片 17" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-18.jpg' | relative_url }}" alt="南京照片 18" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-19.jpg' | relative_url }}" alt="南京照片 19" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-20.jpg' | relative_url }}" alt="南京照片 20" loading="lazy"></div>
            <div class="nanjing-slide"><img src="{{ '/assets/images/nanjing/nanjing-21.jpg' | relative_url }}" alt="南京照片 21" loading="lazy"></div>
        </div>
        <button class="nanjing-control nanjing-prev" type="button" aria-label="上一张">‹</button>
        <button class="nanjing-control nanjing-next" type="button" aria-label="下一张">›</button>
        <div class="nanjing-dots" aria-label="照片导航"></div>
    </div>

    <a href="/news/" class="back-link">← Back to News</a>
</div>

<script>
(function () {
    var carousel = document.querySelector('.nanjing-carousel');
    if (!carousel) return;

    var track = carousel.querySelector('.nanjing-track');
    var slides = Array.prototype.slice.call(carousel.querySelectorAll('.nanjing-slide'));
    var dotsContainer = carousel.querySelector('.nanjing-dots');
    var prevButton = carousel.querySelector('.nanjing-prev');
    var nextButton = carousel.querySelector('.nanjing-next');
    var activeIndex = 0;

    function goTo(index) {
        activeIndex = (index + slides.length) % slides.length;
        track.scrollTo({ left: slides[activeIndex].offsetLeft - track.offsetLeft, behavior: 'smooth' });
        updateDots();
    }

    function updateDots() {
        var dots = dotsContainer.querySelectorAll('.nanjing-dot');
        dots.forEach(function (dot, index) {
            dot.classList.toggle('active', index === activeIndex);
        });
    }

    slides.forEach(function (_, index) {
        var dot = document.createElement('button');
        dot.className = 'nanjing-dot';
        dot.type = 'button';
        dot.setAttribute('aria-label', '查看第 ' + (index + 1) + ' 张照片');
        dot.addEventListener('click', function () {
            goTo(index);
        });
        dotsContainer.appendChild(dot);
    });

    prevButton.addEventListener('click', function () {
        goTo(activeIndex - 1);
    });

    nextButton.addEventListener('click', function () {
        goTo(activeIndex + 1);
    });

    track.addEventListener('scroll', function () {
        window.requestAnimationFrame(function () {
            var trackLeft = track.scrollLeft + track.offsetLeft;
            var closestIndex = slides.reduce(function (closest, slide, index) {
                var currentDistance = Math.abs(slide.offsetLeft - trackLeft);
                var closestDistance = Math.abs(slides[closest].offsetLeft - trackLeft);
                return currentDistance < closestDistance ? index : closest;
            }, activeIndex);
            activeIndex = closestIndex;
            updateDots();
        });
    }, { passive: true });

    updateDots();
})();
</script>
