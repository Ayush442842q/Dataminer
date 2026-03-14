# utils/screen.py — Screen comparison to detect response completion
import pyautogui
import cv2
import numpy as np
import time

def take_screenshot() -> np.ndarray:
    """Take screenshot and return as numpy array."""
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def wait_for_response_complete(timeout: int = 120) -> bool:
    """
    Wait until ChatGPT stops generating.
    Compares screenshots — when screen stops changing, response is done.
    """
    print("  ⏳ Waiting for response to complete...")
    time.sleep(3)  # wait for generation to start

    stable_count    = 0
    required_stable = 4
    check_interval  = 2
    start_time      = time.time()
    prev_screenshot = None

    while time.time() - start_time < timeout:
        current = take_screenshot()

        if prev_screenshot is not None:
            h, w = current.shape[:2]
            # Compare center region of screen where response appears
            region_curr = current[int(h*0.2):int(h*0.85), int(w*0.3):int(w*0.95)]
            region_prev = prev_screenshot[int(h*0.2):int(h*0.85), int(w*0.3):int(w*0.95)]

            diff   = cv2.absdiff(region_curr, region_prev)
            change = np.sum(diff)

            if change < 80000:
                stable_count += 1
                print(f"  📊 Stable count: {stable_count}/{required_stable}")
                if stable_count >= required_stable:
                    print("  ✅ Response complete!")
                    return True
            else:
                stable_count = 0

        prev_screenshot = current
        time.sleep(check_interval)

    print("  ⚠️  Timeout — extracting what's available.")
    return False
