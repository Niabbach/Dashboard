from fastapi import APIRouter, HTTPException
from core.data_loader import TIME, SIGNALS
from models.schemas import SignalSeries

router = APIRouter(prefix="/signals")

@router.get("", response_model=SignalSeries)
def get_signal(name: str):
    if name not in SIGNALS:
        raise HTTPException(404, detail=f"Signal '{name}' not found")

    return {
        "name": name,
        "time": TIME,
        "values": SIGNALS[name]
    }
