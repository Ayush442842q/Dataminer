# scraper/runner.py
import json
import time
from config import PROMPTS_FILE, MAX_RETRIES, MIN_DELAY, MAX_DELAY
from scraper.chatgpt import get_response
from database.operations import save_response, save_failed
from utils.human import random_delay

def load_prompts():
    with open(PROMPTS_FILE, "r") as f:
        return json.load(f)

def save_prompts(prompts):
    with open(PROMPTS_FILE, "w") as f:
        json.dump(prompts, f, indent=2)

def run_all_prompts():
    prompts = load_prompts()
    pending = [p for p in prompts if p["status"] == "pending"]

    print(f"\n  📋 {len(pending)} pending prompt(s) found.\n")

    for i, prompt_obj in enumerate(pending):
        pid    = prompt_obj["id"]
        prompt = prompt_obj["prompt"]
        tags   = prompt_obj.get("tags", [])

        print(f"  {'─'*45}")
        print(f"  🔁 Prompt {i+1}/{len(pending)}  (ID: {pid})")
        print(f"  📝 {prompt[:75]}...")

        success = False
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = get_response(prompt)
                if response:
                    save_response(prompt, response, tags)
                    for p in prompts:
                        if p["id"] == pid:
                            p["status"] = "done"
                    save_prompts(prompts)
                    success = True
                    break
                else:
                    print(f"  ↩️  Empty response — attempt {attempt}/{MAX_RETRIES}")
            except Exception as e:
                print(f"  ⚠️  Error on attempt {attempt}: {e}")

            if attempt < MAX_RETRIES:
                time.sleep(3)

        if not success:
            save_failed(prompt, "Max retries exceeded", tags)
            for p in prompts:
                if p["id"] == pid:
                    p["status"] = "failed"
            save_prompts(prompts)

        if i < len(pending) - 1:
            random_delay(MIN_DELAY, MAX_DELAY)

    print(f"\n  🎉 All prompts processed!")
