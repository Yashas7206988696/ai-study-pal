import random

def motivational_feedback(subject):
    messages = [
        f"Great job studying {subject}! Keep going! 🚀",
        f"You’re making progress in {subject}, don’t stop now! 💪",
        f"{subject} is tough, but you’re tougher. Keep it up! 🔥",
    ]
    return random.choice(messages)
