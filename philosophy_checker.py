# philosophy_checker.py
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

famous_quotes = [('I think, therefore I am', 'René Descartes'), ('The unexamined life is not worth living', 'Socrates'), ('To be is to be perceived', 'George Berkeley'), ('God is dead', 'Friedrich Nietzsche'), ('Man is condemned to be free', 'Jean-Paul Sartre'), ('One cannot step twice into the same river', 'Heraclitus'), ('The only thing I know is that I know nothing', 'Socrates'), ('Hell is other people', 'Jean-Paul Sartre'), ('Liberty consists in doing what one desires', 'John Stuart Mill'), ('Existence precedes essence', 'Jean-Paul Sartre'), ('I can control my passions and emotions if I can understand their nature', 'Spinoza'), ('Life must be understood backward. But it must be lived forward', 'Søren Kierkegaard'), ('No man ever steps in the same river twice', 'Heraclitus'), ('He who opens a school door, closes a prison', 'Victor Hugo'), ('The mind is furnished with ideas by experience alone', 'John Locke'), ('We are what we repeatedly do', 'Aristotle'), ('He who has a why to live can bear almost any how', 'Friedrich Nietzsche'), ('Without music, life would be a mistake', 'Friedrich Nietzsche'), ('Knowledge is power', 'Francis Bacon'), ('Happiness is not an ideal of reason but of imagination', 'Immanuel Kant'), ('Time is a flat circle', 'Friedrich Nietzsche'), ('The more I read, the more I acquire, the more certain I am that I know nothing', 'Voltaire'), ('Happiness depends upon ourselves', 'Aristotle'), ('Happiness is not something ready made. It comes from your own actions', 'Dalai Lama'), ('We are too weak to discover the truth by reason alone', 'St. Augustine'), ('We suffer more often in imagination than in reality', 'Seneca'), ('The brave man is he who overcomes not only his enemies but also his pleasures', 'Democritus'), ('All that we see or seem is but a dream within a dream', 'Edgar Allan Poe'), ('Life is really simple, but we insist on making it complicated', 'Confucius'), ('The greatest wealth is to live content with little', 'Plato')]

quote_texts = [q[0] for q in famous_quotes]
quote_authors = [q[1] for q in famous_quotes]
quote_embeddings = model.encode(quote_texts)

def is_philosophical(sentence):
    sentence_embedding = model.encode([sentence])[0]
    scores = util.cos_sim(sentence_embedding, quote_embeddings)[0]
    max_score = float(scores.max())
    best_idx = int(scores.argmax())
    is_philo = max_score > 0.45
    author = quote_authors[best_idx] if is_philo else "Unknown"
    return is_philo, max_score, author
