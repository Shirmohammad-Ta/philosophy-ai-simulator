
# app.py
import streamlit as st
from sentence_to_model import analyze_philosophical_sentence
from simulation import run_simulation
from visualizer import plot_history, draw_emotion_summary
from quote_db_loader import load_quote_database
from difflib import get_close_matches

st.set_page_config(page_title="Philosophical Emotion Simulator", layout="centered")

st.title("🧠 Philosophical Emotion Simulator")
st.markdown("Enter a philosophical sentence to explore its psychological impact over time.")

# Load the quote database and normalize it
quote_db = load_quote_database()
normalized_quote_db = {q.strip().lower(): a for q, a in quote_db.items()}

user_sentence = st.text_input("📜 Enter your philosophical sentence:")

if user_sentence:
    normalized_input = user_sentence.strip().lower()
    matches = get_close_matches(normalized_input, normalized_quote_db.keys(), n=1, cutoff=0.9)

    if not matches:
        st.error("❌ Error: This sentence is not found in the philosophical database.")
    else:
        matched_sentence = matches[0]
        try:
            model_def = analyze_philosophical_sentence(matched_sentence)
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
