# scraper/browser.py — Opens Chrome on Windows like a human
import subprocess
import time
import pyautogui
import random
from utils.human import human_click, human_type
from config import CHROME_PATH, CHATGPT_URL, LAUNCH_WAIT

def open_chatgpt():
    """
    Human-like flow:
    1. Open Chrome
    2. Wait for it to load
    3. Click URL bar
    4. Type chatgpt.com letter by letter
    5. Press Enter
    6. Wait for page to load
    """
    screen_w, screen_h = pyautogui.size()

    # ── Step 1: Open Chrome ──────────────────────────────────────
    print("  🌐 Opening Chrome...")
    subprocess.Popen([CHROME_PATH, "--new-window"])
    time.sleep(LAUNCH_WAIT)

    # Maximize window
    pyautogui.hotkey("win", "up")
    time.sleep(1)

    # ── Step 2: Click URL bar ────────────────────────────────────
    print("  🖱️  Clicking URL bar...")
    url_x = screen_w // 2
    url_y = 45   # Chrome URL bar on Windows ~45px from top
    human_click(url_x, url_y)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.2)

    # ── Step 3: Type URL letter by letter ────────────────────────
    print("  ⌨️  Typing URL...")
    human_type("chatgpt.com", interval=0.08, variance=0.04)
    time.sleep(random.uniform(0.3, 0.5))

    # ── Step 4: Press Enter ──────────────────────────────────────
    pyautogui.press("enter")
    print("  ↵  Navigating to ChatGPT...")

    # ── Step 5: Wait for page load ───────────────────────────────
    time.sleep(6)
    print("  ✅ ChatGPT ready!")
