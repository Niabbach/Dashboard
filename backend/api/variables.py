from fastapi import APIRouter
from core.data_loader import SIGNALS

router = APIRouter(prefix="/variables")

@router.get("")
def list_variables():
    return sorted(SIGNALS.keys())
