# ChatGPT Dataset Builder — Windows

Automates ChatGPT using real mouse movements and keyboard input to build datasets and save responses to MongoDB. Runs on your actual screen — no browser automation libraries, no bot detection.

---

## How It Works

1. Opens Chrome and navigates to ChatGPT
2. Clicks the input box and types prompts letter by letter (human-like)
3. Waits for the full response to generate
4. Copies the response and saves it to MongoDB
5. Repeats for every prompt in the queue

---

## Requirements

- Windows 10/11
- Python 3.8+
- Google Chrome
- MongoDB (local or Atlas)

---

## Installation

```powershell
# 1. Clone the repo
git clone https://github.com/yourusername/chatgpt-dataset-builder.git
cd chatgpt-dataset-builder

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start MongoDB
mongod
```

---

## Configuration

### Step 1 — Find your screen coordinates
```powershell
python pos.py
```
Move your mouse to the ChatGPT input box and note the X Y values.

### Step 2 — Update `config.py`
```python
INPUT_BOX_X = 1424   # your ChatGPT input box X
INPUT_BOX_Y = 547    # your ChatGPT input box Y
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

```powershell
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
chatgpt-dataset-builder/
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
│   ├── human.py           # Human-like mouse & keyboard
│   ├── screen.py          # Screenshot comparison
│   ├── hasher.py          # SHA256 prompt hashing
│   └── validator.py       # Response validation
└── requirements.txt
```

---

## License

MIT License — free to use, modify, and distribute.
