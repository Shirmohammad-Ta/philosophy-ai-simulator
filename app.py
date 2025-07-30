import streamlit as st
from simulator import run_simulation
from visualizer import plot_history, draw_emotion_summary
from interpreter import interpret_history
from quote_fetcher import search_quote_in_dataset

st.set_page_config(page_title="Philosophy-AI Simulator", layout="centered")

st.title("🧠 Philosophy-AI Emotional Simulator")
st.markdown("Enter a **philosophical quote** to simulate its psychological effect.")

quote = st.text_area("✍️ Enter a philosophical quote:", height=100)

if st.button("🔍 Analyze Quote"):
    if quote.strip():
        # Step 1: Verify if it's a known philosophical quote using Hugging Face API
        found, matched_quote, author = search_quote_in_dataset(quote)

        if found:
            st.success(f"✅ Verified philosophical quote by **{author}**.")
        else:
            st.warning("⚠️ Quote not found in philosophical database. Proceeding anyway...")

        # Step 2: Run the AI simulation
        history = run_simulation(quote)

        # Step 3: Plot dynamics
        plot_history(history)
        draw_emotion_summary(history)

        # Step 4: Show scientific interpretation
        st.subheader("📘 Interpretation")
        interpretation = interpret_history(history)
        st.markdown(interpretation)

st.markdown("---")
st.markdown("<center style='font-size: 14px;'>Created by: Shirmohammad Tavangari ❤️</center>", unsafe_allow_html=True)
