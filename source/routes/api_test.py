from fastapi import APIRouter
import os
from dotenv import load_dotenv

load_dotenv()
serviceName = os.environ.get('SERVICE_TAG')

testApi = APIRouter()

@testApi.post("/apitest")
async def test_api() :

    json_response = {
        'status_code' : '200',
        'status_phrase' : 'OK',
        'service_name' : serviceName,
        'message': 'API TEST SUCCESS'
        }

    return json_response