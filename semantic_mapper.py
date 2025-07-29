# semantic_mapper.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Load sentence embedding model (only once)
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_semantic_weights(sentence):
    """
    Takes a philosophical sentence and returns mapped weights for:
    - Acceptance tendency
    - Identity erosion
    - Emptiness risk
    These are derived from the sentence embedding.
    """
    embedding = model.encode(sentence)

    # Map embedding vector values into meaningful simulation parameters (0.0 - 1.0)
    acceptance_drive = np.clip(np.abs(embedding[10]) % 1.0, 0.1, 0.9)
    identity_erosion = np.clip(np.abs(embedding[20]) % 1.0, 0.1, 0.9)
    emptiness_risk = np.clip(np.abs(embedding[30]) % 1.0, 0.1, 0.9)

    return {
        "acceptance_drive": acceptance_drive,
        "identity_erosion": identity_erosion,
        "emptiness_risk": emptiness_risk
    }
