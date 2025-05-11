import streamlit as st

st.title("Contador ")

if 'count' not in st.session_state:
    st.session_state.count = 0

def incrementar():
    st.session_state.count += 1

def decrementar():
    st.session_state.count -= 1

col1, col2 = st.columns(2)
with col1:
    st.button("Incrementar", on_click=incrementar)
with col2:
    st.button("Decrementar", on_click=decrementar)

st.write("Contador:", st.session_state.count)