# main.py — Entry point (Windows)
import logging
import os
import time
from config import LOG_FILE
from scraper.browser import open_chatgpt
from scraper.runner import run_all_prompts
from database.mongo_client import close_connection
from database.operations import count_by_status

# ── Logging ────────────────────────────────────────────────────────
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# ── Main ───────────────────────────────────────────────────────────
def main():
    print("\n" + "═"*50)
    print("   ChatGPT Dataset Builder  (Windows)")
    print("═"*50)
    print("\n  ⚠️  DO NOT move your mouse while running!")
    print("  ⚠️  Move mouse to TOP-LEFT corner to emergency stop.")
    print("\n  Starting in 5 seconds...\n")
    time.sleep(5)

    try:
        open_chatgpt()
        print("\n  ⏳ Waiting 5s for ChatGPT to fully load...")
        time.sleep(5)
        run_all_prompts()

    except KeyboardInterrupt:
        print("\n  🛑 Stopped by user.")

    except Exception as e:
        logging.error(f"Fatal error: {e}", exc_info=True)

    finally:
        try:
            stats = count_by_status()
            print("\n" + "═"*50)
            print(f"   ✅ Success : {stats['success']}")
            print(f"   ❌ Failed  : {stats['failed']}")
            print(f"   📦 Total   : {stats['total']}")
            print("═"*50 + "\n")
        except:
            pass
        close_connection()

if __name__ == "__main__":
    main()
