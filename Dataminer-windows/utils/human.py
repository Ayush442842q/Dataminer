# utils/human.py — Human-like mouse & keyboard behavior (Windows)
import pyautogui
import random
import time

# Safety: move mouse to corner to abort
pyautogui.FAILSAFE = True
pyautogui.PAUSE    = 0.03

def human_click(x: int, y: int):
    """Move to position and click like a human."""
    pyautogui.moveTo(x, y, duration=random.uniform(0.3, 0.6))
    time.sleep(random.uniform(0.08, 0.18))
    pyautogui.click()
    time.sleep(random.uniform(0.1, 0.2))

def human_type(text: str, interval: float = 0.08, variance: float = 0.04):
    """Type text letter by letter with random delays."""
    for char in text:
        pyautogui.write(char, interval=0)
        delay = interval + random.uniform(0, variance)
        # Occasionally pause slightly longer (thinking pause)
        if random.random() < 0.05:
            delay += random.uniform(0.15, 0.4)
        time.sleep(delay)

def random_delay(min_s: float, max_s: float):
    """Sleep for a random duration."""
    t = random.uniform(min_s, max_s)
    print(f"  ⏳ Waiting {t:.1f}s before next prompt...")
    time.sleep(t)
