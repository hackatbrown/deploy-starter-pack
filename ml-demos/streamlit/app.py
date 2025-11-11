import streamlit as st

st.set_page_config(page_title="Hack@Brown Streamlit")
st.title("🚀 Streamlit Demo")
name = st.text_input("Your team name")
st.write("Hello,", name or "team!")
