# database/operations.py
from datetime import datetime
from database.mongo_client import get_collection
from utils.hasher import hash_prompt
from utils.validator import estimate_tokens

def save_response(prompt: str, response: str, tags: list = []) -> bool:
    collection = get_collection()
    doc_id     = hash_prompt(prompt)

    if collection.find_one({"_id": doc_id}):
        print(f"  ⚠️  Duplicate skipped.")
        return False

    doc = {
        "_id":           doc_id,
        "prompt":        prompt,
        "response":      response,
        "tags":          tags,
        "tokens_approx": estimate_tokens(response),
        "timestamp":     datetime.utcnow().isoformat(),
        "status":        "success",
    }
    collection.insert_one(doc)
    print(f"  💾 Saved to MongoDB!")
    return True

def save_failed(prompt: str, reason: str, tags: list = []):
    collection = get_collection()
    doc_id     = hash_prompt(prompt)
    collection.update_one(
        {"_id": doc_id},
        {"$set": {
            "_id":       doc_id,
            "prompt":    prompt,
            "tags":      tags,
            "status":    "failed",
            "reason":    reason,
            "timestamp": datetime.utcnow().isoformat(),
        }},
        upsert=True
    )
    print(f"  ❌ Logged failure.")

def count_by_status():
    collection = get_collection()
    return {
        "total":   collection.count_documents({}),
        "success": collection.count_documents({"status": "success"}),
        "failed":  collection.count_documents({"status": "failed"}),
    }
