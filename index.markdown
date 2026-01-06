---
layout: default
---

<style>
/* --- 局部样式：仅用于首页轮播图 --- */

/* 轮播容器 */
.slideshow-container {
  max-width: 100%;
  position: relative;
  margin-bottom: 40px;
  border-radius: 8px; 
  overflow: hidden; /* 保证圆角不被图片遮住 */
  box-shadow: 0 4px 12px rgba(0,0,0,0.1); /* 阴影效果 */
}

/* 每一张幻灯片默认隐藏 */
.mySlides {
  display: none;
}

/* 图片样式 */
.banner-img {
  width: 100%;
  height: 350px; /* 这里控制高度，可以自己改 */
  object-fit: cover; /* 保证图片填满不拉伸 */
  vertical-align: middle;
}

/* 淡入动画效果 */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* 右下角的小圆点 */
.dot-container {
  position: absolute;
  bottom: 15px;
  width: 100%;
  text-align: center;
}
.dot {
  height: 10px;
  width: 10px;
  margin: 0 4px;
  background-color: rgba(255,255,255,0.5);
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}
.active {
  background-color: white;
}
</style>

<div class="slideshow-container">

  <div class="mySlides fade">
    <img src="/assets/images/banner1.jpg" class="banner-img" alt="Banner 1">
  </div>

  <div class="mySlides fade">
    <img src="/assets/images/banner2.jpg" class="banner-img" alt="Banner 2">
  </div>

  <div class="mySlides fade">
    <img src="/assets/images/banner4.jpg" class="banner-img" alt="Banner 3">
  </div>

  <div class="dot-container">
    <span class="dot"></span> 
    <span class="dot"></span> 
    <span class="dot"></span>
  </div>

</div>

<script>
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  
  // 隐藏所有图片
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  
  // 索引+1
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  
  // 取消所有圆点的激活状态
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  
  // 显示当前图片，激活当前圆点
  slides[slideIndex-1].style.display = "block";  
  if (dots.length > 0) {
      dots[slideIndex-1].className += " active";
  }
  
  // 每 4000 毫秒 (4秒) 切换一次
  setTimeout(showSlides, 4000); 
}
</script>

<div style="display: flex; flex-wrap: wrap; gap: 30px; justify-content: space-between;">

  <div class="hover-card" style="flex: 1; min-width: 280px; background: #fafafa; padding: 20px; border-radius: 8px;">
    <h3 style="border-bottom: 2px solid #4a90e2; padding-bottom: 10px; margin-top: 0;">📢 NEWS</h3>
    <ul style="padding-left: 20px; line-height: 1.8;">

      <li>
        <strong>2026-01-06:</strong> <br>
        ✈️ 唐展通将于1.7日参加遗传与发育生物学系毕业预答辩。
      </li>
      <li>
        <strong>2026-01-05:</strong> <br>
        ✈️ 唐展通将于1.14日前往广东参加会议。
      </li>
      <li style="margin-top: 15px;">
        <strong>2026-01-05:</strong> <br>
        🎉 我们的实验室网站正式上线了！
      </li>
      <li style="margin-top: 15px;">
        <strong>2025-12-31:</strong> <br>
        📝 展通和浩宇在山东青岛度过了愉快的元旦假期。祝愿新的一年平安健康！
      </li>
      <li style="margin-top: 15px;">
        <strong>2025-12-27:</strong> <br>
        ✈️ 唐展通在深圳参加了中山大学博士面试，为期两天。
      </li>
    </ul>
  </div>

  <div class="hover-card" style="flex: 1; min-width: 280px; background: #fff; padding: 20px; border: 1px solid #eee; border-radius: 8px;">
    <h3 style="border-bottom: 2px solid #e24a4a; padding-bottom: 10px; margin-top: 0;">📚 推荐论文</h3>
    
    <div style="margin-bottom: 15px;">
        <a href="#" style="font-weight: bold; color: #333; text-decoration: none;">Comprehensive maturity of nuclear pore complexes regulates zygotic genome activation</a>
        <div style="font-size: 12px; color: #666; margin-top: 4px;">Shen W, Gong B, Xing C, et al. , <i>Cell</i> (2021)</div>
    </div>
    
    <div style="margin-bottom: 15px;">
        <a href="#" style="font-weight: bold; color: #333; text-decoration: none;">Zygotic Genome Activation in Vertebrates</a>
        <div style="font-size: 12px; color: #666; margin-top: 4px;">Jukam D, Shariati SAM, Skotheim JM., <i>Dev Cell.</i> (2017)</div>
    </div>
  </div>

  <div class="hover-card" style="flex: 1; min-width: 280px; background: #fff; padding: 20px; border: 1px solid #eee; border-radius: 8px;">
    <h3 style="border-bottom: 2px solid #50e3c2; padding-bottom: 10px; margin-top: 0;">🔗 常用链接</h3>
    <ul style="list-style: none; padding: 0;">
      <li style="margin-bottom: 12px;">
        <a href="https://www.seu.edu.cn/" target="_blank" style="text-decoration: none; display: block; padding: 8px; background: #f0f0f0; border-radius: 4px; color: #333;">
          🏫 东南大学官网
        </a>
      </li>
      <li style="margin-bottom: 12px;">
        <a href="https://med.seu.edu.cn/" target="_blank" style="text-decoration: none; display: block; padding: 8px; background: #f0f0f0; border-radius: 4px; color: #333;">
          🧬 东南大学医学院主页
        </a>
      </li>
      <li style="margin-bottom: 12px;">
        <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" style="text-decoration: none; display: block; padding: 8px; background: #f0f0f0; border-radius: 4px; color: #333;">
          📊 pubmed
        </a>
      </li>
      <li style="margin-bottom: 12px;">
        <a href="https://github.com/Newko0213/Newko0213.github.io" target="_blank" style="text-decoration: none; display: block; padding: 8px; background: #f0f0f0; border-radius: 4px; color: #333;">
          💻 GitHub主页（虽然没什么，但我在努力学习！）
        </a>
      </li>
    </ul>
  </div>

</div>

<script>
// 等待页面加载完成
document.addEventListener("DOMContentLoaded", function() {
  // 创建观察者，用于检测元素是否进入视口
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      // 如果元素进入视口（变成可见）
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-visible'); // 添加CSS类，触发动画
      }
    });
  });

  // 找到所有带有 .hover-card 的元素
  const hiddenElements = document.querySelectorAll('.hover-card');
  hiddenElements.forEach((el) => {
    el.classList.add('reveal-on-scroll'); // 初始设为隐藏并下移
    observer.observe(el); // 开始观察
  });
});
</script>