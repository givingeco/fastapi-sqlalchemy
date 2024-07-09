from fastapi import APIRouter
from models.index import transactions
from schemas.index import DeleteAll
from config.db import session
from function.index import db_connection


deleteAllApi = APIRouter()

@deleteAllApi.post("/deleteAll")
async def delete_all (dataIn:DeleteAll):
    
    if dataIn.delete == 'ALL':
        try:
            deleteData = session.query(transactions)

            deleteData.delete()
            session.commit()
        except:
            db_connection()
            return {"statusCode"   : "500",
                    "serviceName"  : "dev-fastapi-sqlalchemy",
                    "errorMessage" : "Database Disconnected and RollBack SUCCESS"}
        finally:
            session.close()
        
        json_response = {
            'statusCode': '200',
            'statusPhrase' : 'OK',
            'message': 'Delete All Transaction success'
            }
        return json_response

    else:
        json_response = {
            'statusCode': '200',
            'statusPhrase' : 'OK',
            'message': 'Delete All Transaction Stop'
            }
        return json_response