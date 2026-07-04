"""
chatbot.py
A simple rule-based chatbot engine.

The bot works by checking the user's message for keywords/patterns and
returning a matching response. No external API or internet connection
is required, which makes this approach fast, free, and fully offline.
"""

import random
import re
from datetime import datetime

# ---------------------------------------------------------------------
# Response bank: each entry maps a set of trigger patterns (regex) to
# a list of possible replies. A random reply is picked so the bot
# doesn't feel too repetitive.
# ---------------------------------------------------------------------
RULES = [
    (r"\b(hi|hello|hey|yo|sup)\b",
     ["Hey there! 👋", "Hello! How can I help you today?", "Hi! What's on your mind?"]),

    (r"\b(bye|goodbye|see ya|see you|farewell)\b",
     ["Goodbye! Have a great day 👋", "See you later!", "Bye! Come back anytime."]),

    (r"\b(thanks|thank you|thx)\b",
     ["You're welcome!", "Anytime!", "No problem at all 🙂"]),

    (r"\bhow are you\b",
     ["I'm just code, but I'm doing great! How about you?", "Running smoothly, thanks for asking!"]),

    (r"\bwhat('s| is) your name\b",
     ["I'm a simple chatbot built for a coding task!", "You can call me ChatBuddy."]),

    (r"\b(joke|funny)\b",
     [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the developer go broke? Because they used up all their cache.",
        "I would tell you a UDP joke, but you might not get it.",
     ]),

    (r"\b(time)\b",
     [f"It's currently {datetime.now().strftime('%H:%M')} on my server clock."]),

    (r"\b(date|today)\b",
     [f"Today's date is {datetime.now().strftime('%B %d, %Y')}."]),

    (r"\b(help|what can you do)\b",
     ["I can chat about greetings, tell jokes, share the time/date, "
      "or just have a casual conversation. Try saying 'joke' or 'hi'!"]),

    (r"\b(sad|upset|down|unhappy)\b",
     ["I'm sorry to hear that. I hope things get better soon 💛",
      "That sounds tough. Want to talk about it, or hear a joke to lighten up?"]),

    (r"\b(happy|great|awesome|good)\b",
     ["That's wonderful to hear! 😄", "Glad things are going well!"]),
]

FALLBACK_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Hmm, I don't have a good answer for that yet. Try asking me for a 'joke' or say 'help'.",
    "Interesting! I'm a simple bot though, so I might not follow everything.",
]


def get_response(user_message: str) -> str:
    """
    Given a user's message, return an appropriate chatbot reply.

    The message is lowercased and checked against each rule's regex
    pattern in order. The first matching rule's reply list is used
    to randomly pick a response. If nothing matches, a fallback
    response is returned.
    """
    if not user_message or not user_message.strip():
        return "Say something and I'll respond!"

    message = user_message.lower()

    for pattern, responses in RULES:
        if re.search(pattern, message):
            return random.choice(responses)

    return random.choice(FALLBACK_RESPONSES)
