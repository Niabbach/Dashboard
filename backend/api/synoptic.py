from fastapi import APIRouter, HTTPException
from core.data_loader import SIGNALS

router = APIRouter(prefix="/synoptic", tags=["Synoptic"])

SYNOPTIC_SIGNALS = {
    "source": "voltage.v",
    "diode": "diode.v",
    "capacitor": "capacitor.v",
    "load": "load.v"
}

@router.get("")
def synoptic(t: int = 0):
    length = len(next(iter(SIGNALS.values())))

    if t < 0 or t >= length:
        raise HTTPException(
            status_code=400,
            detail=f"Index temps invalide (0..{length-1})"
        )

    result = {}
    for name, signal in SYNOPTIC_SIGNALS.items():
        if signal not in SIGNALS:
            result[name] = None
        else:
            result[name] = SIGNALS[signal][t]

    return {
        "time_index": t,
        "values": result
    }