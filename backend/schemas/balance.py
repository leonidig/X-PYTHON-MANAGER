from pydantic import BaseModel, ConfigDict
from typing import Optional
# from datetime import datetime

class BalanceData(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None
    owner: str
    total: float
    date: str
    theme: str
    untouchable: float
    total_sum: Optional[float] = None
    comment: str



class TotalSum(BaseModel):
    current_user: str
    


class Search(BaseModel):
    current_user: str
    comment: str