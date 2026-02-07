import streamlit as st
import pandas as pd
from streamlit_drawable_canvas import st_canvas
from datetime import datetime

# 1. 페이지 설정 (와이드)
st.set_page_config(layout = "wide", page_title = "디지털 갤러리 방명록")

st.title("🎨 디지털 갤러리 & 방명록")

# 2. 사이드바 - 사용자 기본 정보
st.sidebar.header("👤 방문자 정보")
user_name = st.sidebar.text_input("닉네임을 입력하세요", "칼로의 꽃")
visit_date = st.sidebar.date_input("방문 날짜", datetime.now())

# 3. 메인 레이아웃 - 전시 구역
with st.expander("🖼️ 오늘의 전시 작품", expanded = True):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1549490349-8643362247b5", caption = "작품 No.1")
    with col2:
        st.write(
                  """
                  **작품 설명:** viva la vida. 이 작품은 화려한 꽃을 그려낸 그림입니다. 
                  감상을 아래의 방명록에 남겨주세요❤️
                  (이미지 출처: Unplash)
                  """)

st.divider()       # 구분선



# 4. 인터랙티브 요소(그림 그리기 + 폼)
st.header("🖊️ 방명록 남기기")

# 폼을 사용하여 데이터 취합 후 제출
with st.form("guestbook_form"):
    left, right = st.columns([2, 1])
    
    with left:
        st.write("🎨**그림 방명록 (나만의 작품 남기기)**")
        
        # 드로잉 캔버스 추가
        canvas_result = st_canvas(fill_color = "rgba(255, 165, 0, 0.3)",
                                  stroke_width = 3,
                                  stroke_color = "#000000",
                                  background_color = "#ffffff",
                                  height = 300,
                                  width = 600,
                                  drawing_mode = "freedraw",
                                  key = "guestbook_canvas",
                                  )
    
    with right:
        st.write("💬**방문 후기**")
        emoji = st.selectbox("오늘의 무드는?", ['😊', '😍', '🧐', '🌈', '🌿'])
        rating = st.select_slider("전시 후기", options = ['❤️ 사랑스러워요', '💖 감동적이에요', '🌟 눈부셔요', '🎨 예술적이에요', '👍 최고예요'])
        comment = st.text_area("소감 한 마디!")
        
        # 폼 제출 버튼
        submitted = st.form_submit_button("방명록 남기고 가기")

# 5. 제출 완료
if submitted:
    st.balloons()
    st.success(f"감사합니다, {user_name}님! 즐거운 관람이 되셨길 바랍니다.")
    
    st.header("📌 방명록 미리보기")
    visit_col1, visit_col2 = st.columns([1, 2])
    
    with visit_col1:
        if result.image_data is not None:
            st.image(result.image_data, caption=f"{user_name} 님의 작품")
            
    with visit_col2:
        st.markdown(f"""
        **기분:** {emoji} | **만족도:** {rating}  
        **소감:** {comment}  
        ---
        *방문일: {visit_date}*