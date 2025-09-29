import nltk
from nltk.corpus import stopwords

# Try to use NLTK tokenizer, but fall back to a simple whitespace/token filter if resources are missing
try:
    from nltk.tokenize import word_tokenize
    _WORD_TOKENIZE_AVAILABLE = True
except Exception:
    _WORD_TOKENIZE_AVAILABLE = False

# Attempt to download NLTK resources if possible (harmless if already present)
try:
    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)
except Exception:
    pass

def _simple_tokenize(text):
    # Basic fallback: split on non-alphanumeric characters
    import re
    return [t for t in re.split(r"[^A-Za-z0-9]+", text) if t]

def extract_study_tips(text):
    # tokenize using nltk if available, otherwise fallback
    try:
        if _WORD_TOKENIZE_AVAILABLE:
            words = word_tokenize(text)
        else:
            words = _simple_tokenize(text)
    except LookupError:
        words = _simple_tokenize(text)

    # stopwords may still be unavailable; fall back to a small builtin list
    try:
        stops = set(stopwords.words("english"))
    except Exception:
        stops = set(["the", "and", "is", "in", "to", "a", "of", "it"])

    keywords = [w for w in words if w.isalnum() and w.lower() not in stops]
    top_keywords = keywords[:5]
    return [f"Review: {kw}" for kw in top_keywords]
