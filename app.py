# app.py
import streamlit as st
from detect_author_api import detect_author

st.set_page_config(page_title="Philosopher Detector", page_icon="🧠")

st.title("🧠 Who Said This? - Philosophy Quote Detector")

quote = st.text_area("✍️ Enter a famous philosophical quote:")

if st.button("🔍 Detect Author"):
    if quote.strip():
        with st.spinner("Detecting author..."):
            author = detect_author(quote)
        st.success(f"✅ Detected Author: **{author}**")
    else:
        st.warning("⚠️ Please enter a quote to proceed.")
