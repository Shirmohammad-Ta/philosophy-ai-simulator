
from quote_db_loader import load_quote_database
from difflib import get_close_matches

# Load the quote database (2500 quotes)
QUOTE_DB = load_quote_database("quotes.csv")

# Step 1: detect author
def detect_author_nlp(sentence):
    quotes = list(QUOTE_DB.keys())
    match = get_close_matches(sentence.strip(), quotes, n=1, cutoff=0.9)
    if match:
        return QUOTE_DB[match[0]]
    return None

# Step 2: extract emotional variables
def extract_emotional_variables(sentence):
    sentence = sentence.lower()
    variables = []

    emptiness_keywords = ["emptiness", "meaningless", "loneliness", "void", "worthless", "despair", "nihilism", "voidness", "lost"]
    identity_keywords = ["identity", "self", "ego", "personality", "who i am", "individuality", "selfhood", "self-awareness"]
    acceptance_keywords = ["acceptance", "social", "belonging", "community", "rejection", "inclusion", "friendship", "support"]

    if any(word in sentence for word in emptiness_keywords):
        variables.append("E")
    if any(word in sentence for word in identity_keywords):
        variables.append("H")
    if any(word in sentence for word in acceptance_keywords):
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

# Step 4: full analyzer
def analyze_philosophical_sentence(sentence):
    author = detect_author_nlp(sentence)
    if not author:
        raise ValueError("This sentence is not found in the philosophical database.")

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
