from config.db import session
from models.index import transactions
from function.index import db_connection

def db_query_first(table,filter_column,filter_value):
    
    try:
        query = session.query(table).filter(filter_column == filter_value).first()
    except:
        db_connection()
        return {"status_code" : "500",
                        "error_message" : "Database Disconnected and RollBack SUCCESS"}          
    finally:      
        session.close()

    return query