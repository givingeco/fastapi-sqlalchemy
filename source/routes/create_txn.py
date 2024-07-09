from fastapi import APIRouter
from models.index import transactions
from function.index import db_create
from schemas.index import CreateTxn
from datetime import datetime
from pytz import timezone


createTxnApi = APIRouter()

@createTxnApi.post("/createTxn")
async def create_txn (dataIn:CreateTxn):
    
    #Date and Time stampt
    dtFmt = "%Y-%m-%d %H:%M:%S"
    nowTime = datetime.now(timezone('Asia/Bangkok'))
    date=nowTime.strftime(dtFmt)

    newData = transactions(
        amount      = dataIn.amount,
        category    = dataIn.category,
        description = dataIn.description,
        is_income   = dataIn.is_income,
        date        = date
    )

    db_create(newData)

    json_response = {
        'statusCode': '200',
        'statusPhrase' : 'OK',
        'message': 'Transaction create success'
        }
    return json_response