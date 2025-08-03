import streamlit as st
from transformers import pipeline

# تنظیم مدل از Hugging Face (رایگان)
classifier = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis")

def is_philosophical(text):
    keywords = ["philosophy", "ethics", "kant", "nietzsche", "metaphysics"]
    return any(keyword in text.lower() for keyword in keywords)

st.title("🤖 Free Philosophy AI Simulator")
user_input = st.text_area("Enter English text:")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter text!")
    else:
        if is_philosophical(user_input):
            st.success("✅ This text is philosophical!")
            analysis = classifier(user_input)
            st.write("Analysis:", analysis)
        else:
            st.warning("⚠️ This doesn't seem philosophical.")
