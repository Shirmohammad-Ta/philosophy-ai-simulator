# interpreter.py

def interpret_emotional_trajectory(history):
    """
    Analyzes the emotional history and returns a textual scientific-style interpretation.
    """

    H_start, H_end = history["H"][0], history["H"][-1]
    A_start, A_end = history["A"][0], history["A"][-1]
    E_start, E_end = history["E"][0], history["E"][-1]

    analysis = []

    if A_end - A_start > 0.4:
        analysis.append("a strong rise in social conformity tendencies")

    if H_end < 0.4:
        analysis.append("a significant erosion of personal identity")

    if E_end > 0.6:
        analysis.append("an elevated sense of existential emptiness")

    if not analysis:
        return "The subject exhibits emotional balance and resilience over time."

    result = "The simulation suggests " + ", ".join(analysis[:-1])
    if len(analysis) > 1:
        result += ", and " + analysis[-1] + "."

    return result.capitalize()
