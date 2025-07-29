# philosophy_checker.py
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

philosophy_examples = [
    "What is the meaning of life?",
    "The more one sacrifices for social approval, the more empty one feels.",
    "Existence precedes essence.",
    "Freedom is the will to be responsible for ourselves."
]
philosophy_embeddings = model.encode(philosophy_examples)

def is_philosophical(sentence):
    sentence_embedding = model.encode([sentence])[0]
    scores = util.cos_sim(sentence_embedding, philosophy_embeddings)
    max_score = scores.max().item()
    return max_score > 0.45, max_score
