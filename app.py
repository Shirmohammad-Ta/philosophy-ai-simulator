import streamlit as st
from simulator import run_simulation
from visualizer import plot_history, draw_emotion_summary
from interpreter import interpret_history
from quote_fetcher import search_quote_in_dataset

st.set_page_config(page_title="Philosophy AI Simulator", layout="centered")

# === Page Styling ===
st.markdown(
    """
    <style>
    .main { background-color: #f9f9f9; }
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    h1, h2, h3, h4 {
        color: #3B3B98;
    }
    .stTextArea textarea {
        font-size: 16px;
        color: #2C3A47;
    }
    .footer {
        margin-top: 40px;
        text-align: center;
        font-size: 14px;
        color: #888;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# === App Title ===
st.title("🧠 Philosophy-AI Emotional Impact Simulator")
st.markdown("Enter a **philosophical quote** and observe its emotional impact over time, both visually and semantically.")

# === Input Area ===
with st.container():
    user_quote = st.text_area("✒️ *Enter a philosophical quote below*", height=100)

if st.button("🔍 Analyze Quote"):
    if not user_quote.strip():
        st.warning("Please enter a quote.")
    else:
        # Step 1: Find quote or similar
        found, matched_quote, author = search_quote_in_dataset(user_quote)

        with st.expander("🗣️ Quote Attribution"):
            if found and matched_quote:
                st.success(f'✅ Matched to: "{matched_quote}" — *{author}*')
            else:
                st.warning("⚠️ Quote not found in philosophical database. Proceeding anyway...")

        # Step 2: Run simulation
        history = run_simulation(user_quote)

        # Step 3: Visualization
        st.subheader("📊 Emotional Dynamics")
        plot_history(history)

        st.subheader("🎭 Emotional States Summary")
        draw_emotion_summary(history)

        # Step 4: Interpretation
        st.subheader("🧠 Interpretation")
        analysis = interpret_history(history)
        st.markdown(f"```{analysis}```")

# === Footer ===
st.markdown("<hr class='footer'/>", unsafe_allow_html=True)
st.markdown("<p class='footer'>Created by: <strong>Shirmohammad Tavangari</strong></p>", unsafe_allow_html=True)
