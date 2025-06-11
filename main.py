import streamlit as st
import folium
from streamlit_folium import st_folium

# 앱 제목과 헤더
st.markdown("<h1 style='text-align:center; color:#FF4B4B;'>🇪🇸 스페인 여행 가이드 🌟</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>화려하고 직관적인 여행지 정보와 지도를 한눈에!</p>", unsafe_allow_html=True)

# 여행지 데이터
places = {
    "바르셀로나": {
        "coords": [41.3851, 2.1734],
        "desc": "가우디의 걸작 사그라다 파밀리아, 고딕지구, 맛있는 타파스와 활기찬 분위기!",
        "images": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Sagrada_Familia_01.jpg/320px-Sagrada_Familia_01.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Barri_Gotic_Barcelona_2015.jpg/320px-Barri_Gotic_Barcelona_2015.jpg"
        ]
    },
    "마드리드": {
        "coords": [40.4168, -3.7038],
        "desc": "프라도 미술관, 로열 팰리스, 활기 넘치는 스페인 수도.",
        "images": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Palacio_Real_de_Madrid_01.JPG/320px-Palacio_Real_de_Madrid_01.JPG",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Madrid%2C_Plaza_Mayor_01.jpg/320px-Madrid%2C_Plaza_Mayor_01.jpg"
        ]
    },
    "세비야": {
        "coords": [37.3891, -5.9845],
        "desc": "플라멩코의 본고장, 아름다운 알카사르 궁전과 세비야 대성당.",
        "images": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Sevilla_-_Catedral_y_Giralda_02.jpg/320px-Sevilla_-_Catedral_y_Giralda_02.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Sevilla_alcazar.jpg/320px-Sevilla_alcazar.jpg"
        ]
    },
    "그라나다": {
        "coords": [37.1773, -3.5986],
        "desc": "알함브라 궁전, 역사적인 이슬람 건축과 멋진 도시 전경.",
        "images": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Alhambra_view_from_San_Nicolas_-_Granada_-_Spain_2015-12-01_%2810%29.JPG/320px-Alhambra_view_from_San_Nicolas_-_Granada_-_Spain_2015-12-01_%2810%29.JPG",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Alhambra_Granada_Spain_01.jpg/320px-Alhambra_Granada_Spain_01.jpg"
        ]
    },
    "발렌시아": {
        "coords": [39.4699, -0.3763],
        "desc": "미래지향적 건축물인 과학예술시티, 해변과 맛있는 빠에야의 도시.",
        "images": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Ciutat_de_les_Arts_i_les_Ciències%2C_Valencia_01.jpg/320px-Ciutat_de_les_Arts_i_les_Ciències%2C_Valencia_01.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Paella_Valenciana_03.JPG/320px-Paella_Valenciana_03.JPG"
        ]
    }
}

# 사이드바로 여행지 선택
st.sidebar.title("여행지 선택")
selected_place = st.sidebar.radio("가고 싶은 도시를 선택하세요:", list(places.keys()))

# 선택한 여행지 정보 표시
place = places[selected_place]
st.markdown(f"## {selected_place}")
st.markdown(f"_{place['desc']}_")

# 이미지 슬라이더
for img_url in place["images"]:
    st.image(img_url, width=350)

# 지도 생성 및 마커 표시
m = folium.Map(location=place["coords"], zoom_start=13)
for name, info in places.items():
    folium.Marker(
        location=info["coords"],
        popup=f"<b>{name}</b><br>{info['desc']}",
        tooltip=name,
        icon=folium.Icon(color="blue" if name == selected_place else "gray", icon="info-sign")
    ).add_to(m)

st_data = st_folium(m, width=700, height=500)

# 여행 일정 추천 (단순 예시)
st.markdown("---")
st.markdown("### 🗓️ 추천 일정 예시")
st.markdown("""
- **1일차:** 주요 관광지 투어 및 현지 음식 맛보기  
- **2일차:** 박물관 및 문화 체험  
- **3일차:** 자연 경관 산책 및 쇼핑  
- **4일차:** 주변 소도시 방문 및 휴식
""")

# 깔끔한 푸터
st.markdown("""
---
Made with ❤️ by 예준님 존잘존잘 존잘남의 충실한 부하  
""")

