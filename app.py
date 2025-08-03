import streamlit as st
import ollama  # کتابخانه رسمی Ollama

# تنظیمات مدل
MODEL_NAME = "phi3"  # یا "mistral" اگر خواستی تغییر دهی

def analyze_philosophy(text):
    response = ollama.generate(
        model=MODEL_NAME,
        prompt=f"Is this philosophical? Analyze in 2 lines: '{text}'"
    )
    return response["response"]

# رابط کاربری
st.title("🤖 Free Philosophy AI Simulator")
user_input = st.text_area("Enter English text (Philosophical only):")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter text!")
    else:
        with st.spinner("Asking the philosopher..."):
            answer = analyze_philosophy(user_input)
        st.success(answer)
