st.markdown("Multiplication")
M = st.slider("M", 0, 100, 50)
N = st.session_state.N
st.write(f"N * M = {N * M}")