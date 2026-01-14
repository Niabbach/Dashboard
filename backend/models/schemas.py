from pydantic import BaseModel
from typing import List

class SignalSeries(BaseModel):
    name: str
    time: List[float]
    values: List[float]
