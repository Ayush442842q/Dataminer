# utils/validator.py
ERROR_PHRASES = [
    "something went wrong",
    "network error",
    "there was an error",
    "unable to load",
    "too many requests",
]

def is_valid_response(text: str) -> bool:
    if not text or len(text.strip()) < 20:
        return False
    for phrase in ERROR_PHRASES:
        if phrase in text.lower():
            return False
    return True

def estimate_tokens(text: str) -> int:
    return len(text) // 4
