# pos.py — Run this to find coordinates of any element on screen
# Move your mouse to any element and note the X Y values
import pyautogui
import time

print("Move your mouse around to find coordinates.")
print("Press Ctrl+C to stop.\n")

while True:
    x, y = pyautogui.position()
    print(f"X: {x}  Y: {y}", end="\r")
    time.sleep(0.2)
