from fastapi import APIRouter
from models.index import transactions
from function.index import db_query_first
from schemas.index import GetTxn


getTxnApi = APIRouter()

@getTxnApi.post("/getTxn")
async def get_txn (dataIn:GetTxn):
    
    data = db_query_first(transactions,transactions.id,dataIn.id)

    json_response = {
        'statusCode': '200',
        'statusPhrase' : 'OK',
        'message': 'Transaction get success',
        'data': {
            "id": data.id,
            "amount": data.amount,
            "category": data.category,
            "description": data.description,
            "is_income":  data.is_income,
            "date": data.date  
            }
        }
    return json_response