# utils/human.py — Human-like mouse & keyboard behavior (Linux)
import subprocess
import pyautogui
import random
import time

# Safety: move mouse to corner to abort
pyautogui.FAILSAFE = True
pyautogui.PAUSE    = 0.03

def human_click(x: int, y: int):
    """Click at position using xdotool — works on Linux reliably."""
    subprocess.run(['xdotool', 'mousemove', str(x), str(y)])
    time.sleep(random.uniform(0.2, 0.4))
    subprocess.run(['xdotool', 'click', '1'])
    time.sleep(random.uniform(0.1, 0.2))

def human_type(text: str, interval: int = 80, variance: int = 0):
    """
    Type text using xdotool — works on Linux unlike pyautogui.write.
    interval is in milliseconds.
    """
    print(f"  ⌨️  Typing ({len(text)} chars)...")
    subprocess.run([
        'xdotool', 'type',
        '--delay', str(interval),
        '--clearmodifiers',
        text
    ])

def random_delay(min_s: float, max_s: float):
    """Sleep for a random duration."""
    t = random.uniform(min_s, max_s)
    print(f"  ⏳ Waiting {t:.1f}s before next prompt...")
    time.sleep(t)
