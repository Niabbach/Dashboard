from fastapi import APIRouter
from core.data_loader import SIGNALS

router = APIRouter(prefix="/synoptic")

@router.get("")
def simplified_synoptic(t: int = 0):
    def v(sig): return SIGNALS.get(sig, [None])[t]

    return {
        "source": v("voltage.v"),
        "diode": v("diode.v"),
        "capacitor": v("capacitor.v"),
        "load": v("load.v")
    }
