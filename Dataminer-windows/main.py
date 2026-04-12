# main.py — Entry point (Windows)
# Opens Chrome ONCE, then watches for new prompts forever.
# Rajesh feeds prompts via autonomous.py — no new tab each time.

import logging
import os
import time
from config import LOG_FILE
from scraper.browser import open_chatgpt
from scraper.runner import watch_and_run
from database.mongo_client import close_connection
from database.operations import count_by_status

# ── Logging ────────────────────────────────────────────────────────────────────
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    print("\n" + "═" * 50)
    print("   ChatGPT Dataset Builder  (Windows)")
    print("═" * 50)
    print("\n  ⚠️  DO NOT move your mouse while running!")
    print("  ⚠️  Move mouse to TOP-LEFT corner to emergency stop.")
    print("\n  Starting in 5 seconds...\n")
    time.sleep(5)

    try:
        # Open Chrome and navigate to ChatGPT — only once
        open_chatgpt()
        print("\n  ⏳ Waiting 5s for ChatGPT to fully load...")
        time.sleep(5)

        # Stay running — watch for new prompts from Rajesh
        watch_and_run(poll_interval=10)

    except KeyboardInterrupt:
        print("\n  🛑 Stopped by user.")

    except Exception as e:
        logging.error(f"Fatal error: {e}", exc_info=True)

    finally:
        try:
            stats = count_by_status()
            print("\n" + "═" * 50)
            print(f"   ✅ Success : {stats.get('success', 0)}")
            print(f"   ❌ Failed  : {stats.get('failed', 0)}")
            print(f"   📦 Total   : {sum(stats.values())}")
            print("═" * 50 + "\n")
        except Exception:
            pass
        close_connection()
        print("  🔌 MongoDB connection closed.")


if __name__ == "__main__":
    main()