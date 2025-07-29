# interpreter.py

def interpret_graph(history):
    H_final = history["H"][-1]
    A_final = history["A"][-1]
    E_final = history["E"][-1]

    interpretations = []

    # Identity
    if H_final < 0.3:
        interpretations.append("- Severe identity erosion.")
    elif H_final > 0.7:
        interpretations.append("- Strong personal identity maintained.")
    elif 0.3 <= H_final <= 0.7:
        interpretations.append("- Partial identity conflict detected.")

    # Acceptance
    if A_final > 0.7:
        interpretations.append("- High desire for social approval.")
    elif A_final < 0.3:
        interpretations.append("- Low dependence on external validation.")
    else:
        interpretations.append("- Moderate need for social acceptance.")

    # Emptiness
    if E_final > 0.7:
        interpretations.append("- Rising existential emptiness may lead to distress.")
    elif E_final > 0.5:
        interpretations.append("- Noticeable emotional fatigue detected.")
    elif E_final < 0.3:
        interpretations.append("- Emotional stability maintained.")

    return "\n".join(interpretations)
