
# app.py
import streamlit as st
from sentence_to_model import analyze_philosophical_sentence
from simulation import run_simulation
from visualizer import plot_history, draw_emotion_summary

st.set_page_config(page_title="Philosophical Emotion Simulator", layout="centered")

st.title("🧠 Philosophical Emotion Simulator")
st.markdown("Enter a philosophical sentence to explore its psychological impact over time.")

user_sentence = st.text_input("📜 Enter your philosophical sentence:")

if user_sentence:
    try:
        model_def = analyze_philosophical_sentence(user_sentence)
        author = model_def.get("author", "Unknown")
        variables = model_def.get("variables", [])
        eq_str = model_def.get("equation_str", "")
        description = model_def.get("description", "")

        st.markdown(f"**🧾 Author:** *{author}*")
        st.markdown(f"**🔬 Interpreted Variables:** {variables}")
        st.markdown(f"**📐 Equation Used:** `{eq_str}`")
        st.markdown(f"**🧩 Description:** {description}")

        # Run simulation
        history = run_simulation()

        # Show plots
        plot_history(history)
        draw_emotion_summary(history)

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
