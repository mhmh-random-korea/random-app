import random
import streamlit as st

# 1. 웹페이지 기본 설정 및 제목
st.set_page_config(page_title="오늘의 점심 추천", page_icon="🍱")
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘의 점심 메뉴를 뽑아보세요.")

# 2. 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "초밥",
    "짜장면",
    "짬뽕",
    "비빔밥",
    "칼국수",
    "햄버거",
    "쌀국수",
    "마라탕",
    "떡볶이",
    "순대국밥",
    "파스타",
    "샌드위치",
    "치킨",
]

# 3. 버튼 생성 및 클릭 시 동작 설정
if st.button("오늘의 점심 메뉴 뽑기 🎲", use_container_width=True):
  # 리스트에서 무작위로 1개 선택
  today_menu = random.choice(lunch_menus)

  # 추천 결과 화면에 표시
  st.success(f"오늘의 추천 메뉴는 **[{today_menu}]** 입니다! 맛있게 드세요! 😋")
  st.balloons()  # 화면에 풍선이 날아오르는 시각 효과
