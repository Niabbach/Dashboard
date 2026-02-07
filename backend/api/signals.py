from fastapi import APIRouter, HTTPException
from core.data_loader import TIME, SIGNALS
from models.schemas import SignalResponse

router = APIRouter(prefix="/signals", tags=["Signals"])

@router.get("", response_model=SignalResponse)
def get_signal(name: str):
    if name not in SIGNALS:
        raise HTTPException(
            status_code=404,
            detail=f"Signal '{name}' inexistant"
        )

    return {
        "name": name,
        "time": TIME,
        "values": SIGNALS[name]
    }
