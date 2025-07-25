
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
