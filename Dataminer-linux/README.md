# ChatGPT Dataset Builder — Linux

Automates ChatGPT using xdotool for real mouse movements and keyboard input to build datasets and save responses to MongoDB. Runs on your actual screen — no browser automation libraries, no bot detection.

---

## How It Works

1. Opens Chrome with your real profile (already logged in)
2. Navigates to ChatGPT and clicks the input box
3. Types prompts letter by letter using xdotool (human-like)
4. Waits for the full response to generate
5. Copies the response using xclip and saves to MongoDB
6. Repeats for every prompt in the queue

---

## Requirements

- Ubuntu / Debian Linux
- Python 3.8+
- Google Chrome
- MongoDB
- xdotool + xclip

---

## Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/chatgpt-dataset-builder-linux.git
cd chatgpt-dataset-builder-linux

# 2. Install system dependencies
sudo apt-get install xdotool xclip python3-tk python3-dev

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Start MongoDB
sudo mkdir -p /data/db && sudo chown -R $USER /data/db
mongod   # run in a separate terminal
```

---

## Configuration

### Step 1 — Find your screen coordinates
```bash
python pos.py
```
Move your mouse to the ChatGPT input box and note the X Y values.

### Step 2 — Update `config.py`
```python
INPUT_BOX_X  = 837    # your ChatGPT input box X
INPUT_BOX_Y  = 922    # your ChatGPT input box Y
CHROME_PROFILE = "/home/yourusername/.config/google-chrome"
```

### Step 3 — Add your prompts
Copy `prompts/prompts.example.json` to `prompts/prompts.json` and add your prompts:
```json
[
  {
    "id": 1,
    "prompt": "Explain Newton's three laws of motion.",
    "tags": ["physics", "science"],
    "status": "pending"
  }
]
```

---

## Run

```bash
source venv/bin/activate
python main.py
```

---

## MongoDB Document Structure

```json
{
  "_id": "<sha256 hash of prompt>",
  "prompt": "Your prompt here",
  "response": "ChatGPT response here",
  "tags": ["tag1", "tag2"],
  "tokens_approx": 320,
  "timestamp": "2026-03-14T10:00:00",
  "status": "success"
}
```

---

## Prompt Status Values

| Status | Meaning |
|--------|---------|
| `pending` | Not yet processed |
| `done` | Successfully saved to DB |
| `failed` | Max retries exceeded |

---

## Safety

- Move mouse to **top-left corner** to emergency stop
- Do **not** touch mouse while script is running
- Keep screen on and unlocked

---

## Project Structure

```
chatgpt-dataset-builder-linux/
├── config.py              # All settings
├── main.py                # Entry point
├── pos.py                 # Coordinate finder helper
├── prompts/
│   ├── prompts.json           # Your prompt queue (git ignored)
│   └── prompts.example.json   # Template
├── scraper/
│   ├── browser.py         # Opens Chrome, navigates to ChatGPT
│   ├── chatgpt.py         # Types prompts, copies responses
│   └── runner.py          # Loops through prompt queue
├── database/
│   ├── mongo_client.py    # MongoDB connection
│   └── operations.py      # Save, deduplicate, log failures
├── utils/
│   ├── human.py           # xdotool mouse & keyboard control
│   ├── screen.py          # Screenshot comparison
│   ├── hasher.py          # SHA256 prompt hashing
│   └── validator.py       # Response validation
└── requirements.txt
```

---

## License

MIT License — free to use, modify, and distribute.
