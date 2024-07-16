from fastapi import APIRouter
import os
from config.db import session
from models.index import transactions
from dotenv import load_dotenv

load_dotenv()
serviceName = os.environ.get('SERVICE_TAG')

getAllApi = APIRouter()

@getAllApi.post("/getAll")
async def get_all() :

    data = session.query(transactions).all()
    session.close()
    totalData = len(data)

    output = []
    #print(output)

    for txnData in data:
        
        subData = {
            'id': txnData.id,
            'description': txnData.description,
            'category': txnData.category
            }

        output += [subData]
    
    #print(output)

    json_response = {
        'statusCode' : '200',
        'statusPhrase' : 'OK',
        'message': 'Get All SUCCESS',
        'toalData': totalData,
        'data': output
        }

    return json_response