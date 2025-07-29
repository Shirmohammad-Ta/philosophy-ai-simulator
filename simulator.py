# simulator.py
import numpy as np

def run_simulation(sentence, steps=51):
    """
    Simulates the emotional variables H (Identity), A (Acceptance), and E (Emptiness)
    over a number of time steps in response to a philosophical sentence.
    """
    np.random.seed(len(sentence))  # Deterministic based on sentence length

    H = [1.0]  # Identity
    A = [0.0]  # Acceptance
    E = [0.0]  # Emptiness

    for t in range(1, steps):
        delta_A = 0.02 + np.random.uniform(0, 0.01)
        delta_H = -0.015 - np.random.uniform(0, 0.01)
        delta_E = 0.015 + np.random.uniform(0, 0.015)

        A.append(min(1.0, A[-1] + delta_A))
        H.append(max(0.0, H[-1] + delta_H))
        E.append(min(1.0, E[-1] + delta_E if H[-1] < 0.5 else E[-1]))

    return {"H": H, "A": A, "E": E}
