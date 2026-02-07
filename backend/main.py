from fastapi import FastAPI
from core.data_loader import SIGNALS, TIME

app = FastAPI(title="API Dymola Simulator")

@app.get("/hello")
def hello():
    return {"message": "Hello Dymola 👋"}

@app.get("/variables")
def variables():
    return {"variables": list(SIGNALS.keys())}

@app.get("/signals")
def get_signal(name: str):
    if name not in SIGNALS:
        return {"error": f"Signal '{name}' introuvable"}
    return {
        "name": name,
        "time": TIME,
        "values": SIGNALS[name]
    }

@app.get("/synoptic")
def synoptic(t: int = 0):
    if t < 0 or t >= len(TIME):
        return {"error": "Index temporel invalide"}

    return {
        "time": TIME[t],
        "values": {
            "voltage": SIGNALS.get("voltage.v", [])[t],
            "diode": SIGNALS.get("diode.v", [])[t],
            "capacitor": SIGNALS.get("capacitor.v", [])[t],
            "load": SIGNALS.get("load.v", [])[t],
        }
    }
