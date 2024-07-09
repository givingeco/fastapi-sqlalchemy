from pydantic import BaseModel

class CreateTxn (BaseModel):
    amount: float
    category: str
    description: str
    is_income: str
    #date: str