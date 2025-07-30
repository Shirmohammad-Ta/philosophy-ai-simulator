# app.py

import streamlit as st
from simulator import run_simulation
from visualizer import plot_history, draw_emotion_summary
from interpreter import interpret_graph
from philosophy_db import is_in_database

st.set_page_config(page_title="Philosophy-AI", layout="centered")

st.title("🧠 Philosophy-AI Simulator")
st.markdown("Enter a philosophical quote to simulate its psychological effects.")

# Input from user
quote = st.text_area("🖋️ Enter your philosophical quote here:", height=120)

if st.button("🔍 Analyze Quote"):
    if not quote.strip():
        st.warning("Please enter a valid quote.")
    else:
        # Step 1: Check if it's in our philosophy database
        found = is_in_database(quote)
        if found:
            st.success("✅ Verified philosophical quote.")
        else:
            st.info("⚠️ Not found in philosophical database. Proceeding anyway...")

        # Step 2: Run simulation
        history = run_simulation(quote)

        # Step 3: Visualize
        st.subheader("📈 Emotional Simulation Graph")
        plot_history(history)

        # Step 4: Emotional State Summary
        draw_emotion_summary(history)

        # Step 5: Interpretation
        st.subheader("🧠 Scientific Interpretation")
        interpretation = interpret_graph(history)
        st.code(interpretation, language="markdown")

# Footer
st.markdown("<br><center style='opacity:0.6;'>Created by: Shirmohammad Tavangari</center>", unsafe_allow_html=True)
