
# app.py
import streamlit as st
from sentence_to_model import analyze_philosophical_sentence
from simulation import run_simulation
from visualizer import plot_history, draw_emotion_summary
from quote_db_loader import load_quote_database

st.set_page_config(page_title="Philosophical Emotion Simulator", layout="centered")

st.title("🧠 Philosophical Emotion Simulator")
st.markdown("Enter a philosophical sentence to explore its psychological impact over time.")

# Load the quote database and normalize it
quote_db = load_quote_database()
normalized_quote_db = {q.strip().lower(): a for q, a in quote_db.items()}

user_sentence = st.text_input("📜 Enter your philosophical sentence:")

if user_sentence:
    normalized_input = user_sentence.strip().lower()
    if normalized_input not in normalized_quote_db:
        st.error("❌ Error: This sentence is not found in the philosophical database.")
    else:
        try:
            model_def = analyze_philosophical_sentence(user_sentence)
            author = model_def["author"]
            variables = model_def["variables"]
            eq_str = model_def["equation_str"]
            description = model_def["description"]

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
