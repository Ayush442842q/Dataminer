# database/operations.py
import json
import os
from datetime import datetime
from database.mongo_client import get_collection
from utils.hasher import hash_prompt
from utils.validator import estimate_tokens

# ── Rajesh output file ─────────────────────────────────────────────────────────
# Writes to dataminer_output.json so Rajesh can read responses live.
# Points to the agent-01 folder where autonomous.py lives.
RAJESH_DIR     = r"H:\Future\agent-01"
DATAMINER_OUT  = os.path.join(RAJESH_DIR, "dataminer_output.json")

def _write_for_rajesh(prompt: str, response: str, tags: list):
    """Write latest response to dataminer_output.json for Rajesh to pick up."""
    data = {
        "prompt":    prompt,
        "response":  response,
        "tags":      tags,
        "timestamp": datetime.utcnow().isoformat(),
        "source":    "dataminer",
    }
    try:
        with open(DATAMINER_OUT, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  📡 Sent to Rajesh!")
    except Exception as e:
        print(f"  ⚠️  Could not write dataminer_output.json: {e}")


# ── Original functions (unchanged except save_response) ───────────────────────

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

    # ── Send to Rajesh ─────────────────────────────────────────────────────────
    _write_for_rajesh(prompt, response, tags)

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