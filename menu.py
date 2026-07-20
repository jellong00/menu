import streamlit as st

st.set_page_config(page_title="오늘 저녁 메뉴 추천", page_icon="🍽️")

st.title("🍽️ 오늘 저녁 메뉴 추천!")
st.write("아래 버튼을 눌러서 오늘 저녁 메뉴를 추천받아보세요 😋")

if "revealed" not in st.session_state:
    st.session_state.revealed = False

if st.button("메뉴 추천받기 🍲", use_container_width=True):
    st.session_state.revealed = True

if st.session_state.revealed:

    st.image("KakaoTalk_20260720_194437742.jpg", use_container_width=True)
    st.markdown("<h2 style='text-align:center;'>메뉴는 무슨 메뉴야 ㅋㅋㅋ</h2>", unsafe_allow_html=True)

    if st.button("다시하기"):
        st.session_state.revealed = False
        st.rerun()
