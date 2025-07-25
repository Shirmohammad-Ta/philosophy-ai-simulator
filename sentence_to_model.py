
# sentence_to_model.py

def analyze_sentence(sentence):
    if "social acceptance" in sentence.lower() and "emptiness" in sentence.lower():
        return {
            "variables": ["H", "A", "V", "E"],
            "equation": lambda A, V, beta=1.0: beta * A * V,
            "description": "Sacrificing identity (V) for acceptance (A) increases existential emptiness (E)."
        }
    else:
        raise ValueError("Model for this sentence not defined yet.")
