# utils/hasher.py
import hashlib

def hash_prompt(prompt: str) -> str:
    return hashlib.sha256(prompt.strip().lower().encode()).hexdigest()
