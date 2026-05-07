import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.intents import check_intents
from src.preprocess import preprocess

with open("data/faqs.json") as f:
    faqs = json.load(f)

faq_lookup = []
training_questions = []

for index, faq in enumerate(faqs):
    phrases = [faq["question"], *faq.get("patterns", [])]
    for phrase in phrases:
        training_questions.append(preprocess(phrase))
        faq_lookup.append(index)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_questions)


def get_best_match(user_input):
    intent_response = check_intents(user_input)
    if intent_response:
        return intent_response

    user_processed = preprocess(user_input)
    user_vector = vectorizer.transform([user_processed])

    similarities = cosine_similarity(user_vector, X)
    best_score = similarities.max()
    best_index = similarities.argmax()

    if best_score < 0.2:
        return "I am not sure I understood that. Please ask again in English or Roman Urdu, for example: 'order track kesy karun' or 'return policy kya hai'."

    return faqs[faq_lookup[best_index]]["answer"]
