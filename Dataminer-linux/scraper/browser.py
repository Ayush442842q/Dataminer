# scraper/browser.py — Opens Chrome on Linux like a human
import subprocess
import time
import random
from utils.human import human_click, human_type
from config import CHROME_PATH, CHROME_PROFILE, LAUNCH_WAIT
import pyautogui

def open_chatgpt():
    """
    Human-like flow:
    1. Open Chrome with real profile (already logged in)
    2. Wait for it to load
    3. Click URL bar
    4. Type chatgpt.com letter by letter
    5. Press Enter
    6. Wait for page to load
    """
    screen_w, screen_h = pyautogui.size()

    # ── Step 1: Open Chrome with your real profile ───────────────
    print("  🌐 Opening Chrome...")
    subprocess.Popen([
        CHROME_PATH,
        f'--user-data-dir={CHROME_PROFILE}',
        '--profile-directory=Default',
        '--new-window',
        '--disable-blink-features=AutomationControlled'
    ])
    time.sleep(LAUNCH_WAIT)

    # Maximize window
    subprocess.run(['xdotool', 'key', 'super+Up'])
    time.sleep(1)

    # ── Step 2: Click URL bar ────────────────────────────────────
    print("  🖱️  Clicking URL bar...")
    url_x = screen_w // 2
    url_y = 55   # Chrome URL bar on Linux ~55px from top
    human_click(url_x, url_y)
    time.sleep(0.3)
    subprocess.run(['xdotool', 'key', 'ctrl+a'])
    time.sleep(0.2)

    # ── Step 3: Type URL ─────────────────────────────────────────
    print("  ⌨️  Typing URL...")
    human_type("chatgpt.com", interval=80)
    time.sleep(random.uniform(0.3, 0.5))

    # ── Step 4: Press Enter ──────────────────────────────────────
    subprocess.run(['xdotool', 'key', 'Return'])
    print("  ↵  Navigating to ChatGPT...")

    # ── Step 5: Wait for page load ───────────────────────────────
    time.sleep(6)
    print("  ✅ ChatGPT ready!")
