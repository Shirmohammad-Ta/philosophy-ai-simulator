# visualizer.py
import matplotlib.pyplot as plt
import streamlit as st

def plot_history(history):
    fig, ax = plt.subplots()
    ax.plot(history["H"], label="Identity (H)", marker='o')
    ax.plot(history["A"], label="Acceptance (A)", marker='x')
    ax.plot(history["E"], label="Emptiness (E)", marker='s')
    ax.set_xlabel("Time Step")
    ax.set_ylabel("Value")
    ax.set_title("Emotional Dynamics Over Time")
    ax.legend()
    st.pyplot(fig)

def describe_emotional_state(H, A, E):
    if H < 0.3 and A > 0.7 and E > 0.6:
        return "😟 Overconformity – Anxiety from sacrificing identity for acceptance."
    elif H > 0.7 and A < 0.3 and E < 0.4:
        return "🙂 Self-assured – Strong identity and low external dependence."
    elif H > 0.5 and E > 0.5:
        return "😐 Inner tension – Balanced identity but feeling drained."
    elif E > 0.7:
        return "😶 Existential emptiness – Deep psychological fatigue."
    elif H > 0.6 and A > 0.6:
        return "🫂 Healthy engagement – Maintaining identity while being accepted."
    else:
        return "🧘 Undefined emotional state – Mixed signals."

def draw_emotion_summary(history):
    st.subheader("🧠 Overall Emotional Summary")

    summary_states = []
    for t in [0, 15, 30, 50]:
        H = history["H"][t]
        A = history["A"][t]
        E = history["E"][t]
        state = describe_emotional_state(H, A, E)
        summary_states.append(state)

    # Pick the most frequent emotional state as the dominant one
    from collections import Counter
    most_common_state = Counter(summary_states).most_common(1)[0][0]

    st.markdown(f"### 🧭 Dominant State: {most_common_state}")
