# semantic_mapper.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_semantic_weights(sentence):
    """
    Converts philosophical sentence to 3 dynamic weights:
    - acceptance_drive
    - identity_erosion
    - emptiness_risk
    Applies stronger differentiation for real variance in output
    """
    embedding = model.encode(sentence)

    # More robust fingerprinting
    base = np.abs(embedding)
    acceptance_drive = np.clip(np.mean(base[0:20]) * 2.2, 0.0, 1.0)
    identity_erosion = np.clip(np.mean(base[20:40]) * 2.5, 0.0, 1.0)
    emptiness_risk = np.clip(np.mean(base[40:60]) * 2.8, 0.0, 1.0)

    return {
        "acceptance_drive": acceptance_drive,
        "identity_erosion": identity_erosion,
        "emptiness_risk": emptiness_risk
    }
