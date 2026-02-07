from fastapi import APIRouter
from core.data_loader import SIGNALS

router = APIRouter(prefix="/variables", tags=["Variables"])

@router.get("")
def list_variables():
    return {
        "count": len(SIGNALS),
        "variables": sorted(SIGNALS.keys())
    }
