# app.py
import streamlit as st
from simulator import run_simulation
from visualizer import plot_history, draw_emotion_summary
from interpreter import interpret_graph
from philosophy_checker import is_philosophical
from quote_attributor import guess_author

st.set_page_config(page_title="Philosophical Sentence Emotional Impact Simulator", layout="wide")
st.title("🌀 Philosophical Sentence Emotional Impact Simulator")

# User Input
sentence = st.text_area("🖋️ Enter a philosophical sentence", height=100)

if sentence:
    with st.expander("🔍 Step 1: Is this philosophical?"):
        is_philo, score, author_from_check = is_philosophical(sentence)
        st.markdown(f"**Philosophical?** {'✅ Yes' if is_philo else '❌ No'} (Confidence: {score:.2f})")

    with st.expander("🧠 Step 2: Author Identification"):
        author_ai = guess_author(sentence)
        st.markdown(f"**From Knowledge Base:** _{author_from_check}_")
        st.markdown(f"**From API Guess:** _{author_ai}_")

    if is_philo:
        with st.expander("📈 Step 3: Emotional Simulation"):
            history = run_simulation(sentence)
            plot_history(history)
            draw_emotion_summary(history)

        with st.expander("🧾 Step 4: Interpretation"):
            interpretation = interpret_graph(history)
            st.markdown(f"```\n{interpretation}```")
    else:
        st.warning("This sentence was not identified as philosophical. Try another.")
else:
    st.info("Enter a sentence above to begin.")

# Footer at bottom center
st.markdown(
    "<div style='text-align: center; padding-top: 50px;'>"
    "<hr style='border: none; border-top: 1px solid #ccc;'>"
    "<p style='color: gray;'>Created by: <strong>Shirmohammad Tavangari</strong></p>"
    "</div>",
    unsafe_allow_html=True
)
