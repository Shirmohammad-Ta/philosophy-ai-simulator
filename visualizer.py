# visualizer.py
import matplotlib.pyplot as plt
import streamlit as st

def plot_history(history):
    fig, ax = plt.subplots()
    ax.plot(history["H"], label="Identity (H)", linewidth=2)
    ax.plot(history["A"], label="Acceptance (A)", linewidth=2)
    ax.plot(history["E"], label="Emptiness (E)", linewidth=2, linestyle='--')
    ax.set_xlabel("Time Step")
    ax.set_ylabel("Value")
    ax.set_title("🧠 Emotional Dynamics Over Time")
    ax.legend()
    st.pyplot(fig)

# 🧠 تفسیر عمیق‌تر حالات احساسی:
def describe_emotional_state(H, E, A):
    if A > 0.75 and H < 0.4:
        return "😟 Overconformity – Anxiety from sacrificing identity for acceptance."
    elif E > 0.7 and H < 0.3:
        return "😶 Existential Collapse – Deep emptiness due to lost self."
    elif H > 0.6 and E > 0.6:
        return "😐 Identity Conflict – Strong self with internal struggle."
    elif H > 0.5 and E < 0.3 and A > 0.5:
        return "😄 Inner Harmony – Balanced acceptance with strong self."
    elif H < 0.3 and A < 0.3 and E > 0.6:
        return "🥀 Withdrawal – Emotional shutdown and isolation."
    else:
        return "🧘 Undefined emotional state – Mixed signals."

def draw_emotion_summary(history):
    st.subheader("🧠 Emotional States at Key Time Points")
    for t in [0, 15, 30, 50]:
        H = history["H"][t]
        E = history["E"][t]
        A = history["A"][t]
        state = describe_emotional_state(H, E, A)
        st.markdown(f"**Step {t}** → {state}")
