# ─────────────────────────────────────────
#  config.py  –  Central settings (Windows)
# ─────────────────────────────────────────

# MongoDB
MONGO_URI        = "mongodb://localhost:27017"
MONGO_DB         = "chatgpt_dataset"
MONGO_COLLECTION = "responses"

# ChatGPT URL
CHATGPT_URL      = "https://chatgpt.com"

# ── Screen Coordinates ─────────────────────────────────────────────
# Run pos.py to find these for your screen
INPUT_BOX_X      = 1424   # ChatGPT input box X
INPUT_BOX_Y      = 547    # ChatGPT input box Y

# ── Typing behavior ────────────────────────────────────────────────
TYPING_INTERVAL  = 0.08   # seconds between each keypress
TYPING_VARIANCE  = 0.04   # random extra delay per key

# ── Timing ─────────────────────────────────────────────────────────
MIN_DELAY        = 6      # min wait between prompts (seconds)
MAX_DELAY        = 13     # max wait between prompts (seconds)
RESPONSE_TIMEOUT = 120    # max seconds to wait for full response
LAUNCH_WAIT      = 4      # seconds after opening Chrome

# ── Paths ──────────────────────────────────────────────────────────
PROMPTS_FILE     = "prompts/prompts.json"
LOG_FILE         = "logs/run.log"

# ── Retries ────────────────────────────────────────────────────────
MAX_RETRIES      = 3

# ── Chrome (Windows path) ──────────────────────────────────────────
CHROME_PATH      = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
