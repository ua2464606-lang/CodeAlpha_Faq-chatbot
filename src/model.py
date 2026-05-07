from src.preprocess import preprocess
from src.intents import check_intents
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

with open("data/faqs.json") as f:
    faqs = json.load(f)

questions = [preprocess(faq["question"]) for faq in faqs]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)


def get_best_match(user_input):

    # 👉 1. Check intents first
    intent_response = check_intents(user_input)
    if intent_response:
        return intent_response

    # 👉 2. Then do FAQ matching
    user_processed = preprocess(user_input)
    user_vector = vectorizer.transform([user_processed])

    similarities = cosine_similarity(user_vector, X)
    best_score = similarities.max()
    best_index = similarities.argmax()

    if best_score < 0.2:
        return "I'm not sure I understand. Can you rephrase?"

    return faqs[best_index]["answer"]