# app.py
import streamlit as st
from detect_author import detect_author
from sentence_to_model import analyze_sentence
from rl_agent import train_agent, run_simulation
from visualizer import plot_history, draw_emotion_summary

st.set_page_config(page_title="Philosophical Simulator", layout="centered")
st.title("🧠 Philosophy-to-Emotion Simulator")

st.markdown("✏️ Enter a philosophical quote below. The system will guess the author and simulate its emotional effects.")

user_input = st.text_area("Philosophical Sentence", height=100)

if st.button("Simulate") and user_input.strip():
    with st.spinner("Detecting author and running simulation..."):
        author = detect_author(user_input)
        st.markdown(f"👤 **Detected Author:** `{author}`")

        try:
            model_def = analyze_sentence(user_input)
            model, env = train_agent()
            history = run_simulation(model, env)
            st.success("Simulation complete.")
            plot_history(history)
            draw_emotion_summary(history)
        except Exception as e:
            st.error(str(e))
