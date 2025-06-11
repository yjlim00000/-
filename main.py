import streamlit as st
import folium
from streamlit_folium import st_folium

# 앱 제목
st.title("스페인 여행 가이드 🏖️🇪🇸")

st.markdown("""
스페인의 멋진 여행지들을 소개해드립니다!  
지도에서 위치를 클릭하면 자세한 설명을 확인할 수 있어요.
""")

# 스페인 주요 여행지 데이터 (위도, 경도, 설명)
places = [
    {"name": "바르셀로나", "lat": 41.3851, "lon": 2.1734,
     "desc": "가우디의 걸작 사그라다 파밀리아, 고딕지구, 맛있는 타파스와 활기찬 분위기!"},
    {"name": "마드리드", "lat": 40.4168, "lon": -3.7038,
     "desc": "프라도 미술관, 로열 팰리스, 활기 넘치는 스페인 수도."},
    {"name": "세비야", "lat": 37.3891, "lon": -5.9845,
     "desc": "플라멩코의 본고장, 아름다운 알카사르 궁전과 세비야 대성당."},
    {"name": "그라나다", "lat": 37.1773, "lon": -3.5986,
     "desc": "알함브라 궁전, 역사적인 이슬람 건축과 멋진 도시 전경."},
    {"name": "발렌시아", "lat": 39.4699, "lon": -0.3763,
     "desc": "미래지향적 건축물인 과학예술시티, 해변과 맛있는 빠에야의 도시."}
]

# 지도 초기 위치 및 줌 설정
m = folium.Map(location=[40.0, -3.0], zoom_start=6)

# 마커 추가
for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 스트림릿에 폴리움 지도 표시
st_data = st_folium(m, width=700, height=500)

# 추가로 여행 팁이나 정보도 보여줄 수 있음
st.markdown("""
---
### 여행 팁!  
- 스페인에서는 점심과 저녁 사이에 시에스타(낮잠)를 즐기는 문화가 있습니다.  
- 타파스 바를 찾아 다양한 스페인 음식을 경험해 보세요!  
- 여름에는 해변도 좋지만, 봄과 가을에 방문하면 더 쾌적합니다.
""")

