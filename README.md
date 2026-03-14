# DataMiner 🤖

> Automate ChatGPT to build your own AI datasets — no API key required.

Dataminer is an open-source desktop automation tool that types prompts into ChatGPT like a human, waits for responses, and saves them directly to MongoDB. Built with Python, it runs on your real screen using mouse and keyboard simulation — making it completely undetectable.

---

## ✨ Features

- 🖱️ **Human-like automation** — moves cursor and types letter by letter with random delays
- 🧠 **Smart deduplication** — SHA256 hashing prevents saving duplicate responses
- 📋 **Prompt queue system** — JSON-based queue with status tracking (pending / done / failed)
- 🔄 **Resume from crash** — picks up exactly where it left off if interrupted
- 🗄️ **MongoDB storage** — structured dataset with tags, timestamps, and token estimates
- 🏷️ **Tag system** — organize prompts by category for cleaner datasets
- 🪟 **Cross-platform** — separate builds for Windows and Linux

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Chrome (logged into ChatGPT)
- MongoDB running locally

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/PromptHarvester.git
cd PromptHarvester

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Linux — Install extra system tools
```bash
sudo apt-get install xdotool xclip python3-tk python3-dev
```

---

## ⚙️ Configuration

### Step 1 — Find your screen coordinates
```bash
python pos.py
```
Move your mouse to the ChatGPT input box and note the `X` and `Y` values shown.

### Step 2 — Update `config.py`
```python
INPUT_BOX_X = 1424   # X coordinate of ChatGPT input box
INPUT_BOX_Y = 547    # Y coordinate of ChatGPT input box
```

### Step 3 — Add your prompts
Copy the example file and fill in your prompts:
```bash
cp prompts/prompts.example.json prompts/prompts.json
```

```json
[
  {
    "id": 1,
    "prompt": "Explain Newton's three laws of motion with real-world examples.",
    "tags": ["physics", "science"],
    "status": "pending"
  }
]
```

---

## ▶️ Run

```bash
python main.py
```

The script will:
1. Open Chrome and navigate to ChatGPT
2. Click the input box and type your prompt
3. Wait for the full response
4. Save it to MongoDB
5. Repeat for every prompt in the queue

---

## 🗄️ MongoDB Schema

Each saved response follows this structure:

```json
{
  "_id": "a3f8c2d1e4b7...",
  "prompt": "Explain Newton's three laws of motion",
  "response": "Newton's first law states that...",
  "tags": ["physics", "science"],
  "tokens_approx": 320,
  "timestamp": "2026-03-14T10:00:00",
  "status": "success"
}
```

---

## 📁 Project Structure

```
PromptHarvester/
├── config.py                    # All settings in one place
├── main.py                      # Entry point
├── pos.py                       # Screen coordinate finder
├── prompts/
│   ├── prompts.json             # Your prompt queue (git ignored)
│   └── prompts.example.json     # Template
├── scraper/
│   ├── browser.py               # Opens Chrome, navigates to ChatGPT
│   ├── chatgpt.py               # Types prompts, copies responses
│   └── runner.py                # Manages the prompt queue loop
├── database/
│   ├── mongo_client.py          # MongoDB connection handler
│   └── operations.py            # Save, deduplicate, log failures
├── utils/
│   ├── human.py                 # Human-like mouse & keyboard simulation
│   ├── screen.py                # Screenshot comparison for response detection
│   ├── hasher.py                # SHA256 prompt hashing
│   └── validator.py             # Response validation
└── requirements.txt
```

---

## ⚠️ Important Notes

- **Do not move your mouse** while the script is running
- Move mouse to the **top-left corner** to emergency stop at any time
- Keep your screen **on and unlocked** during the run
- Make sure you are **logged into ChatGPT** in Chrome before running
- MongoDB must be **running in the background**

---

## 🔄 Prompt Status System

| Status | Meaning |
|--------|---------|
| `pending` | Not yet processed |
| `done` | Successfully saved to MongoDB |
| `failed` | Max retries exceeded — logged for review |

Crashed mid-run? Just run again — completed prompts are skipped automatically.

---

## 🛠️ Built With

- [PyAutoGUI](https://pyautogui.readthedocs.io/) — Mouse and keyboard control
- [xdotool](https://www.semicomplete.com/projects/xdotool/) — Linux input simulation
- [OpenCV](https://opencv.org/) — Screen comparison for response detection
- [PyMongo](https://pymongo.readthedocs.io/) — MongoDB integration
- [MongoDB](https://www.mongodb.com/) — Dataset storage

---

## 📄 License

MIT License — free to use, modify, and distribute. See [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or want to suggest a feature, open an issue.

---

## ⭐ Support

If this project helped you, consider giving it a star on GitHub!
