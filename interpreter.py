# interpreter.py

def interpret_graph(history):
    H = history["H"]
    A = history["A"]
    E = history["E"]

    delta_H = H[-1] - H[0]
    delta_A = A[-1] - A[0]
    delta_E = E[-1] - E[0]

    interpretation = "🧠 Interpretation:\n"

    if delta_H < -0.5 and delta_E > 0.5:
        interpretation += "- Severe identity erosion with rising existential emptiness.\n"
    elif delta_H < -0.3:
        interpretation += "- Identity is declining noticeably.\n"
    if delta_A > 0.5:
        interpretation += "- Strong tendency toward social approval.\n"
    if delta_E > 0.4:
        interpretation += "- Emptiness rising significantly, potential for psychological distress.\n"
    if delta_H > 0 and delta_A > 0:
        interpretation += "- Positive integration of identity and acceptance observed.\n"

    if interpretation.strip() == "🧠 Interpretation:":
        interpretation += "- No significant emotional shift detected."

    return interpretation
