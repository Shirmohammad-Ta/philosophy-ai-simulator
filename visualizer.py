# visualizer.py
import matplotlib.pyplot as plt
import streamlit as st

def plot_history(history):
    fig, ax = plt.subplots()
    ax.plot(history["H"], label="Identity (H)")
    ax.plot(history["A"], label="Acceptance (A)")
    ax.plot(history["E"], label="Emptiness (E)")
    ax.set_xlabel("Time Step")
    ax.set_ylabel("Value")
    ax.set_title("Emotional Dynamics Over Time")
    ax.legend()
    st.pyplot(fig)



def describe_emotional_state(H, E):
    if H > 0.7 and E > 0.5:
        return "😟 Early anxiety – Feeling pressure to be accepted."
    elif H > 0.4 and E > 0.4:
        return "😐 Inner conflict – Sacrificing slowly, feeling confused."
    elif H < 0.3 and E > 0.6:
        return "😶 Emptiness – Lost identity in exchange for approval."
    elif H > 0.4 and E < 0.3:
        return "🙂 Balance – Learned to maintain self while connecting."
    else:
        return "🧘 Undefined emotional state."

def draw_emotion_summary(history):
    st.subheader("🧠 Emotional States at Key Time Points")
    for t in [0, 15, 30, 50]:
        H = history["H"][t]
        E = history["E"][t]
        state = describe_emotional_state(H, E)
        st.markdown(f"**Step {t}** → {state}")
