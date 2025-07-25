
import streamlit as st
from sentence_to_model import analyze_sentence
from rl_agent import train_agent, run_simulation
from visualizer import plot_history

st.set_page_config(page_title="Philosophy Emotional Simulator", layout="centered")

st.title("🧠 Philosophy-to-Emotion Simulator")
st.markdown("Enter a philosophical sentence in English:")

sentence = st.text_input("💬 Philosophical sentence:")

if st.button("Simulate!"):
    try:
        model_def = analyze_sentence(sentence)
        model, env = train_agent()
        history = run_simulation(model, env)
        st.success("Simulation complete.")
        plot_history(history)
    except Exception as e:
        st.error(str(e))
