# database/mongo_client.py
from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

_client     = None
_collection = None

def get_collection():
    global _client, _collection
    if _collection is None:
        _client     = MongoClient(MONGO_URI)
        db          = _client[MONGO_DB]
        _collection = db[MONGO_COLLECTION]
        print(f"  ✅ MongoDB connected → {MONGO_DB}.{MONGO_COLLECTION}")
    return _collection

def close_connection():
    global _client
    if _client:
        _client.close()
        print("  🔌 MongoDB connection closed.")
