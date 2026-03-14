# scraper/chatgpt.py — Core ChatGPT interaction (Windows)
import pyautogui
import pyperclip
import time
import random
from utils.human import human_click, human_type
from utils.screen import wait_for_response_complete
from utils.validator import is_valid_response
from config import INPUT_BOX_X, INPUT_BOX_Y, TYPING_INTERVAL, TYPING_VARIANCE

def click_input_box():
    """Click the ChatGPT input box using exact coordinates."""
    print(f"  🖱️  Clicking input box...")
    human_click(INPUT_BOX_X, INPUT_BOX_Y)
    time.sleep(0.5)
    # Clear any existing text
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.2)
    pyautogui.press("delete")
    time.sleep(0.3)

def type_prompt(prompt: str):
    """Type the prompt letter by letter like a human."""
    print(f"  ⌨️  Typing prompt ({len(prompt)} chars)...")
    human_type(prompt, interval=TYPING_INTERVAL, variance=TYPING_VARIANCE)
    time.sleep(0.5)

def send_prompt():
    """Press Enter to send."""
    pyautogui.press("enter")
    print("  📤 Prompt sent!")
    time.sleep(2)

def copy_response() -> str:
    """
    Copy the full page text and extract the last response.
    Uses Ctrl+A then Ctrl+C on the page.
    """
    time.sleep(1.5)

    # Click somewhere in the response area (center of page)
    screen_w, screen_h = pyautogui.size()
    pyautogui.click(screen_w // 2, screen_h // 2)
    time.sleep(0.5)

    # Select all and copy
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

    full_text = pyperclip.paste()
    return extract_last_response(full_text)

def extract_last_response(full_text: str) -> str:
    """Extract the last assistant response from full page text."""
    if not full_text:
        return ""

    lines = [l.strip() for l in full_text.strip().split("\n") if l.strip()]
    if not lines:
        return ""

    # Take last large block of text as the response
    result = []
    for line in reversed(lines):
        if len(line) < 3:
            continue
        result.insert(0, line)
        if len(" ".join(result)) > 300:
            break

    return "\n".join(result).strip()

def get_response(prompt: str) -> str:
    """Full pipeline: click → type → send → wait → copy."""
    click_input_box()
    type_prompt(prompt)
    send_prompt()
    wait_for_response_complete()
    response = copy_response()

    if not is_valid_response(response):
        print("  ⚠️  Response validation failed.")
        return ""

    print(f"  📥 Got response ({len(response)} chars).")
    return response
