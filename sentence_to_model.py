# sentence_to_model.py
from difflib import get_close_matches

# Sample quote-author database
quote_db = {
    "Hell is other people.": "Jean-Paul Sartre",
    "That which does not kill us makes us stronger.": "Friedrich Nietzsche",
    "Man is nothing but what he makes of himself.": "Jean-Paul Sartre",
    "Happiness depends upon ourselves.": "Aristotle",
    "I think, therefore I am.": "René Descartes",
    "The more one sacrifices themselves for social acceptance, the more existential emptiness they feel.": "Anonymous"
}

# Step 1: detect author
def detect_author_nlp(sentence):
    quotes = list(quote_db.keys())
    match = get_close_matches(sentence, quotes, n=1, cutoff=0.6)
    if match:
        return quote_db[match[0]]
    return "Unknown"

# Step 2: extract emotional variables
def extract_emotional_variables(sentence):
    sentence = sentence.lower()
    variables = []
    if "emptiness" in sentence or "meaningless" in sentence:
        variables.append("E")
    if "identity" in sentence or "self" in sentence:
        variables.append("H")
    if "acceptance" in sentence or "social" in sentence:
        variables.append("A")
    return variables

# Step 3: construct math model
def construct_equation(variables):
    if set(variables) == {"A", "V"}:
        return lambda A, V, beta=1.0: beta * A * V, "E = β × A × V"
    elif set(variables) == {"A", "H"}:
        return lambda A, H, beta=1.0: beta * A * (1 - H), "E = β × A × (1 - H)"
    elif "E" in variables:
        return lambda E, decay=0.05: E * (1 - decay), "E = E × (1 - decay)"
    else:
        return None, "Equation not found"

# Step 4: smart analyzer
def analyze_philosophical_sentence(sentence):
    author = detect_author_nlp(sentence)
    variables = extract_emotional_variables(sentence)
    eq_func, eq_str = construct_equation(variables)

    if eq_func is None:
        raise ValueError("Couldn't construct equation for this sentence.")

    return {
        "author": author,
        "variables": variables,
        "equation_func": eq_func,
        "equation_str": eq_str,
        "description": f"Derived from variables {variables} → {eq_str}"
    }
