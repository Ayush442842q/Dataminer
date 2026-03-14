# ─────────────────────────────────────────
#  config.py  –  Central settings (Linux)
# ─────────────────────────────────────────

# MongoDB
MONGO_URI        = "mongodb://localhost:27017"
MONGO_DB         = "chatgpt_dataset"
MONGO_COLLECTION = "responses"

# ChatGPT URL
CHATGPT_URL      = "https://chatgpt.com"

# ── Screen Coordinates ─────────────────────────────────────────────
# Run pos.py to find these for your screen
INPUT_BOX_X      = 837    # ChatGPT input box X (run pos.py to find)
INPUT_BOX_Y      = 922    # ChatGPT input box Y (run pos.py to find)

# ── Typing behavior ────────────────────────────────────────────────
TYPING_INTERVAL  = 80     # milliseconds between each keypress (xdotool)

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

# ── Chrome (Linux path) ────────────────────────────────────────────
CHROME_PATH      = "google-chrome"
CHROME_PROFILE   = "/home/ayushsingh/.config/google-chrome"
