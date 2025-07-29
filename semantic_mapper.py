# semantic_mapper.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Load model only once
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_semantic_weights(sentence):
    """
    Maps a philosophical sentence to 3 semantic influence weights:
    - acceptance_drive: openness to external validation
    - identity_erosion: loss of core self
    - emptiness_risk: emotional depletion
    Derived from deeper aggregation of embedding
    """
    embedding = model.encode(sentence)

    acceptance_drive = np.clip(np.mean(np.abs(embedding[5:15])) % 1.0, 0.1, 0.9)
    identity_erosion = np.clip(np.mean(np.abs(embedding[15:25])) % 1.0, 0.1, 0.9)
    emptiness_risk = np.clip(np.mean(np.abs(embedding[25:35])) % 1.0, 0.1, 0.9)

    return {
        "acceptance_drive": acceptance_drive,
        "identity_erosion": identity_erosion,
        "emptiness_risk": emptiness_risk
    }
