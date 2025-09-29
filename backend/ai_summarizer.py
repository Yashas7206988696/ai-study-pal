def summarize_text(text, max_sentences=2):
    sentences = text.split(". ")
    return ". ".join(sentences[:max_sentences]) + ("." if sentences else "")
