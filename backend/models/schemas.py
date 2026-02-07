from pydantic import BaseModel
from typing import List

class SignalResponse(BaseModel):
    name: str
    time: List[float]
    values: List[float]
