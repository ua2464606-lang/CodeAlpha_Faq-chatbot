import random
import re

intents = {
    "greeting": {
        "patterns": [
            "hi",
            "hello",
            "hey",
            "salam",
            "assalamualaikum",
            "assalam o alaikum",
            "aoa",
            "kia hal hai",
            "kya haal hai",
            "kesy ho",
            "kaise ho"
        ],
        "responses": [
            "Hello! How can I help you?",
            "Hi there! What can I do for you?",
            "Walikum assalam! Aap apna question English ya Roman Urdu me pooch sakte hain."
        ]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "allah hafiz", "khuda hafiz", "phir milte hain"],
        "responses": [
            "Goodbye!",
            "See you later!",
            "Take care!"
        ]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "shukriya", "jazakallah", "mehrbani", "thankx"],
        "responses": [
            "You're welcome!",
            "No problem!",
            "Glad I could help!"
        ]
    }
}


def check_intents(user_input):
    user_input = user_input.lower()

    for intent in intents.values():
        for pattern in intent["patterns"]:
            if re.search(rf"(?<!\w){re.escape(pattern)}(?!\w)", user_input):
                return random.choice(intent["responses"])

    return None
