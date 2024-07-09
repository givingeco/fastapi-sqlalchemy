from fastapi import APIRouter
from models.index import transactions
from schemas.index import DeleteTxns
from config.db import session


deleteTxnsApi = APIRouter()

@deleteTxnsApi.post("/deleteTxns")
async def delete_txns (dataIn:DeleteTxns):
    
    # DELETE Multiple Record
    deleteTxn = transactions.__table__.delete().where(transactions.amount == dataIn.amount)
    session.execute(deleteTxn)
    session.commit()
    session.close()
    
    json_response = {
        'statusCode': '200',
        'statusPhrase' : 'OK',
        'message': 'Multiple Transactions delete success',
        }
    return json_response