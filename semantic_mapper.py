# semantic_mapper.py
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_semantic_weights(sentence):
    embedding = model.encode(sentence)

    acceptance_keywords = ["acceptance", "approval", "others", "love", "social"]
    identity_keywords = ["truth", "self", "authentic", "real", "integrity"]
    emptiness_keywords = ["empty", "void", "meaningless", "nothing", "lost"]

    def keyword_score(keywords):
        score = 0
        for word in keywords:
            sub_embed = model.encode(word)
            score += np.dot(embedding, sub_embed)
        return score / len(keywords)

    a_score = keyword_score(acceptance_keywords)
    h_score = keyword_score(identity_keywords)
    e_score = keyword_score(emptiness_keywords)

    total = a_score + h_score + e_score
    return {
        "acceptance_drive": a_score / total,
        "identity_erosion": 1 - (h_score / total),
        "emptiness_risk": e_score / total
    }
