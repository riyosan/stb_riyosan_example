import streamlit as st
import streamlit_book as stb

# Set wide display
st.set_page_config(layout="wide")

# Set shared sidebar
st.sidebar.markdown("## Shared Sidebar")
N = st.sidebar.slider("N", 0, 100, 50)
st.session_state.N = N
# Set multipage
save_answers = False
stb.set_chapter_config(path="pages/",
                       save_answers=save_answers,
                       )