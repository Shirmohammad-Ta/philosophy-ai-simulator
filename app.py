import streamlit as st
from simulator import run_simulation
from visualizer import plot_history, draw_emotion_summary
from interpreter import interpret_history
from quote_fetcher import search_quote_in_dataset

st.set_page_config(page_title="Philosophy AI Simulator", layout="centered")

st.title("🧠 Philosophy-AI Emotional Impact Simulator")
st.markdown("Enter a **philosophical quote** and observe its emotional impact over time.")

# Input
user_quote = st.text_area("✒️ Enter a philosophical quote:", height=100)

if st.button("🔍 Analyze Quote"):
    if not user_quote.strip():
        st.warning("Please enter a quote.")
    else:
        # Step 1: Find quote or similar
        found, matched_quote, author = search_quote_in_dataset(user_quote)

        if found:
            st.success(f"✅ Matched to: "{matched_quote}" — *{author}*")
        else:
            st.warning("⚠️ Quote not found in philosophical database. Proceeding anyway...")

        # Step 2: Run simulation
        history = run_simulation(user_quote)

        # Step 3: Visualization
        plot_history(history)
        draw_emotion_summary(history)

        # Step 4: Interpretation
        st.subheader("🧠 Interpretation:")
        analysis = interpret_history(history)
        st.markdown(analysis)

# Footer
st.markdown("<hr style='margin-top: 40px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px;'>Created by: <strong>Shirmohammad Tavangari</strong></p>", unsafe_allow_html=True)
