from fastapi import APIRouter
from models.index import transactions
from function.index import db_update
from schemas.index import UpdateTxn
from config.db import session


updateTxnApi = APIRouter()

@updateTxnApi.post("/updateTxn")
async def update_txn (dataIn:UpdateTxn):
    
    # Update Member Info
    updateData = session.query(transactions).filter(transactions.id == dataIn.id).first()
    
    updateData.amount = dataIn.amount
    
    db_update()

    json_response = {
        'statusCode': '200',
        'statusPhrase' : 'OK',
        'message': 'Transaction update success'
        }
    return json_response