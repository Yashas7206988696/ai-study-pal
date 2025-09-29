<<<<<<< HEAD
def summarize_text(text, max_sentences=2):
    sentences = text.split(". ")
    return ". ".join(sentences[:max_sentences]) + ("." if sentences else "")
=======
def summarize_text(text, max_sentences=2):
    sentences = text.split(". ")
    return ". ".join(sentences[:max_sentences]) + ("." if sentences else "")
>>>>>>> e60b692163850de42bdbad1168022c06d8707106
