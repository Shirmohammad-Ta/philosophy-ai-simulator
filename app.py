
# app.py
import streamlit as st

st.set_page_config(page_title="Philosophy Emotional Simulator", layout="centered")

st.title("🧠 Philosophy-to-Emotion Simulator")

st.markdown("""
This tool helps you enter a philosophical sentence and observe its impact on the human mind.
""")

sentence = st.text_area("✍️ Enter your philosophical sentence:")

if st.button("Analyze:"):
    st.success("In the initial version, only your sentence was received! 👀 The model will be launched soon.")
