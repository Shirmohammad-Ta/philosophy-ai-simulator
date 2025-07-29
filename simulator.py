# simulator.py
import numpy as np
from semantic_mapper import extract_semantic_weights

def run_simulation(sentence, steps=51):
    """
    Simulates emotional dynamics over time (H, A, E) based on a philosophical sentence.
    The semantic meaning of the sentence influences the simulation parameters.
    """

    # Extract semantic weights from the sentence
    weights = extract_semantic_weights(sentence)
    acceptance_drive = weights["acceptance_drive"]
    identity_erosion = weights["identity_erosion"]
    emptiness_risk = weights["emptiness_risk"]

    H = [1.0]  # Identity
    A = [0.0]  # Acceptance
    E = [0.0]  # Emptiness

    for t in range(1, steps):
        # Adjusted delta based on semantic weights
        delta_A = 0.015 + acceptance_drive * 0.01 + np.random.uniform(0, 0.005)
        delta_H = -0.01 - identity_erosion * 0.01 - np.random.uniform(0, 0.005)
        delta_E = emptiness_risk * 0.02 + (0.01 if H[-1] < 0.5 else 0)

        A.append(min(1.0, A[-1] + delta_A))
        H.append(max(0.0, H[-1] + delta_H))
        E.append(min(1.0, E[-1] + delta_E if H[-1] < 0.6 else E[-1]))

    return {"H": H, "A": A, "E": E}
