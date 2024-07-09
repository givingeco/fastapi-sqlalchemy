from fastapi import APIRouter
from models.index import transactions
from schemas.index import DeleteTxn
from config.db import session


deleteTxnApi = APIRouter()

@deleteTxnApi.post("/deleteTxn")
async def delete_txn (dataIn:DeleteTxn):
    
    # DELETE Single Record
    deleteData = session.query(transactions).filter(transactions.id == dataIn.id).first()
    session.delete(deleteData)
    session.commit()
    session.close()

    json_response = {
        'statusCode': '200',
        'statusPhrase' : 'OK',
        'message': 'Transaction delete success',
        }
    return json_response