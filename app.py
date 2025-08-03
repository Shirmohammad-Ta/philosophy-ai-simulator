import streamlit as st
from transformers import pipeline

# مدل سبک‌تر برای اجرا روی فضای ابری
@st.cache_resource
def load_model():
    return pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

classifier = load_model()

def is_philosophical(text):
    keywords = ["philosophy", "ethics", "kant", "nietzsche", "metaphysics"]
    return any(keyword in text.lower() for keyword in keywords)

# رابط کاربری
st.title("🤖 Free Philosophy AI Simulator")
user_input = st.text_area("Enter English text:")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter text!")
    else:
        if is_philosophical(user_input):
            st.success("✅ This text is philosophical!")
            with st.spinner("Analyzing..."):
                analysis = classifier(user_input[:512])  # محدودیت طول متن
            st.write("Analysis:", analysis)
        else:
            st.warning("⚠️ This doesn't seem philosophical.")
