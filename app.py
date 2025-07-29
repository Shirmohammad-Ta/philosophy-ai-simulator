# app.py
import streamlit as st
from simulator import run_simulation
from visualizer import plot_history, draw_emotion_summary
from quote_author_finder import guess_author_by_web

st.set_page_config(page_title="Philosophical Insight AI", layout="centered")

st.title("🧠 Philosophical Insight through AI")
st.markdown("Enter a philosophical sentence and see its psychological evolution and author attribution.")

# User input
sentence = st.text_input("📜 Enter your philosophical sentence:", "")

if sentence:
    with st.spinner("Running simulation and analyzing..."):
        # Run simulation
        history = run_simulation(sentence)

        # Plot emotional variables
        plot_history(history)

        # Show emotion summary
        draw_emotion_summary(history)

        # Show guessed author
        author = guess_author_by_web(sentence)
        st.markdown("---")
        st.subheader("🖋️ Quote Attribution")
        st.markdown(f"**Guessed Author:** {author}")
