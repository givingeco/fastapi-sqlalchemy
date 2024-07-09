from pydantic import BaseModel

class UpdateTxn (BaseModel):
    id: int
    amount: float