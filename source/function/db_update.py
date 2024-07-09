from config.db import session
from function.index import db_connection

def db_update() :
    try:
        session.commit()
    except:
        db_connection()
        return {"status_code" : "500",
                "error_message" : "Database Disconnected and RollBack SUCCESS"}
    finally:
        session.close()