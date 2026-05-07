import random

intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "salam", "assalamualaikum"],
        "responses": [
            "Hello! 👋 How can I help you?",
            "Hi there! 😊 What can I do for you?",
            "Hey! Ask me anything."
        ]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you"],
        "responses": [
            "Goodbye! 👋",
            "See you later!",
            "Take care!"
        ]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "shukriya"],
        "responses": [
            "You're welcome! 😊",
            "No problem!",
            "Glad I could help!"
        ]
    }
}

def check_intents(user_input):
    user_input = user_input.lower()

    for intent in intents.values():
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    return None