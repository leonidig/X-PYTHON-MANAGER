from pydantic import BaseModel, ConfigDict
from typing import Optional

class BalanceData(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None
    owner: str
    total: float

class TotalSum(BaseModel):
    current_user: str