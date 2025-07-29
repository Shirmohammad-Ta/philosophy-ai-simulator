# simulator.py
import numpy as np
from semantic_mapper import extract_semantic_weights

def run_simulation(sentence, steps=51):
    weights = extract_semantic_weights(sentence)
    acceptance_drive = weights["acceptance_drive"]
    identity_erosion = weights["identity_erosion"]
    emptiness_risk = weights["emptiness_risk"]

    H = [1.0]
    A = [0.0]
    E = [0.0]

    for t in range(1, steps):
        prev_H = H[-1]
        prev_A = A[-1]
        prev_E = E[-1]

        delta_A = np.tanh(acceptance_drive * (1 - prev_A)) * 0.1
        delta_H = -np.power(identity_erosion * (1 - prev_A), 1.2) * 0.08
        delta_E = (emptiness_risk * (1 - prev_H) + prev_A * 0.3) * 0.06

        A_new = np.clip(prev_A + delta_A, 0.0, 1.0)
        H_new = np.clip(prev_H + delta_H, 0.0, 1.0)
        E_new = np.clip(prev_E + delta_E, 0.0, 1.0)

        A.append(A_new)
        H.append(H_new)
        E.append(E_new)

    return {"H": H, "A": A, "E": E}
