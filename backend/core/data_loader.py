import json
from pathlib import Path

DATA_PATH = Path("../data/ACDC_timeseries.json")

with open(DATA_PATH, "r") as f:
    RAW = json.load(f)

TIME = RAW["time"]
SIGNALS = RAW["signals"]
