import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="입력한 데이터로 그래프 그리기", page_icon="📊", layout="centered")

st.title("📊 실시간 그래프 생성기")
st.markdown("예준님이 입력한 데이터를 기반으로 멋진 그래프를 그려드립니다! 😎")

# -------------------------------
# 1. 데이터 입력 방식 선택
# -------------------------------
input_method = st.radio("데이터 입력 방법 선택:", ["표 직접 입력", "CSV 업로드"])

# -------------------------------
# 2. 데이터 입력 처리
# -------------------------------
if input_method == "표 직접 입력":
    st.markdown("### ✍️ 데이터 입력 (최소 두 열 이상)")
    sample_data = {
        "항목": ["A", "B", "C"],
        "값": [10, 30, 20]
    }
    df = st.data_editor(pd.DataFrame(sample_data), use_container_width=True, num_rows="dynamic")

elif input_method == "CSV 업로드":
    uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.stop()

# -------------------------------
# 3. 그래프 유형 선택 및 출력
# -------------------------------
if 'df' in locals() and df is not None:
    st.markdown("## 🎨 그래프 유형 선택")
    graph_type = st.selectbox("원하는 그래프를 선택하세요", ["선 그래프", "막대 그래프", "파이 차트"])

    x_axis = st.selectbox("X축 (항목)", df.columns, key="x")
    y_axis = st.selectbox("Y축 (값)", df.columns, key="y")

    st.markdown("---")
    st.markdown("## 📈 결과 그래프")

    fig, ax = plt.subplots()

    if graph_type == "선 그래프":
        sns.lineplot(data=df, x=x_axis, y=y_axis, marker="o", ax=ax)
    elif graph_type == "막대 그래프":
        sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif graph_type == "파이 차트":
        labels = df[x_axis].astype(str)
        values = df[y_axis]
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        ax.axis("equal")

    st.pyplot(fig)

