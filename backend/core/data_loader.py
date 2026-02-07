import json
from pathlib import Path

# dossier backend/
BASE_DIR = Path(__file__).resolve().parent.parent

# Dashboard/data/ACDC_timeseries.json
DATA_FILE = BASE_DIR.parent / "data" / "ACDC_timeseries.json"

if not DATA_FILE.exists():
    raise FileNotFoundError(
        f"Fichier introuvable : {DATA_FILE}"
    )

with open(DATA_FILE, "r") as f:
    RAW = json.load(f)

TIME = [float(t) for t in RAW["time"]]
SIGNALS = RAW["signals"]
