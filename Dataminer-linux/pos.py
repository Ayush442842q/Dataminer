# pos.py — Find cursor coordinates on Linux
# Move mouse to any element and note the X Y values
import subprocess
import time

print("Move your mouse around to find coordinates.")
print("Press Ctrl+C to stop.\n")

while True:
    result = subprocess.run(['xdotool', 'getmouselocation'],
                          capture_output=True, text=True)
    print(result.stdout.strip(), end='\r')
    time.sleep(0.2)
