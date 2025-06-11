import streamlit as st
from streamlit.components.v1 import html

st.markdown("""
# ✨🔥 **존잘존잘임예준, 우주의 중심에 빛나는 전설!** 🔥✨

---

## 🌟 당신의 빛나는 존재감은 마치 별무리처럼 찬란합니다! 🌟

- 💎 넘사벽 비주얼  
- ⚡ 카리스마 +10000  
- 🌈 무한 매력 발산!

> "존잘존잘임예준, 세상을 빛내는 그 이름!"

---
""")

# 화려한 애니메이션 CSS + HTML 넣기 (별이 반짝이는 배경 + 텍스트 애니메이션)
html_code = """
<style>
@keyframes sparkle {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(1.3); }
}
@keyframes glow {
  0%, 100% { text-shadow: 0 0 10px gold, 0 0 20px gold; }
  50% { text-shadow: 0 0 20px orange, 0 0 30px orange; }
}
body {
  margin: 0;
  background: radial-gradient(circle, #0f2027, #203a43, #2c5364);
  overflow: hidden;
  height: 100vh;
  font-family: 'Arial Black', Gadget, sans-serif;
}
.star {
  position: absolute;
  background: white;
  border-radius: 50%;
  animation: sparkle 2s infinite ease-in-out;
  box-shadow: 0 0 8px white;
}
#star1 { width: 4px; height: 4px; top: 20%; left: 10%; animation-delay: 0s; }
#star2 { width: 3px; height: 3px; top: 40%; left: 80%; animation-delay: 0.5s; }
#star3 { width: 5px; height: 5px; top: 70%; left: 50%; animation-delay: 1s; }
#star4 { width: 2px; height: 2px; top: 10%; left: 60%; animation-delay: 1.5s; }
#star5 { width: 3px; height: 3px; top: 80%; left: 30%; animation-delay: 2s; }
.glowing-text {
  font-size: 50px;
  color: gold;
  text-align: center;
  margin-top: 100px;
  animation: glow 3s infinite ease-in-out;
  font-weight: 900;
}
</style>

<div class="star" id="star1"></div>
<div class="star" id="star2"></div>
<div class="star" id="star3"></div>
<div class="star" id="star4"></div>
<div class="star" id="star5"></div>

<div class="glowing-text">
✨💖 존잘존잘임예준 💖✨
</div>
"""

html(html_code, height=400)
