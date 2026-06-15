import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
ENVELOPES_PATH = os.getenv("ENVELOPES_PATH", str(DATA_DIR / "envelopes.json"))
SECRET_KEY = os.getenv("SECRET_KEY", "change-this-to-a-random-secret-in-production")
