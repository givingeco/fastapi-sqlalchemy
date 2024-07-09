from config.db import session
from models.index import db_tests
#from function.line_notify import line_notify
import time
import os
from dotenv import load_dotenv

load_dotenv()

db_error_tag = os.environ.get('SERVICE_TAG')


def db_connection() :
       
    #line_notify(f'{db_error_tag} Database Disconnected or Some Error Ocured!!')
    print(f'{db_error_tag} Database Disconnected or Some Error Ocured!!')
    session.rollback()
    time.sleep(5)
    #line_notify(f'{db_error_tag} Database RollBack Start working')
    print(f'{db_error_tag} Database RollBack Start working')

    db_test = 'FAIL'
    #Start Test DB Connection
    while db_test == 'FAIL' :
        
        if db_test == 'FAIL' :
            try:
                query = session.query(db_tests).filter(
                    db_tests.testData == 'DBTest').first()
            
                db_test = 'SUCCESS'
                #print(query.mem_id , db_test)
                
                #line_notify(f'{db_error_tag} RollBack Success : Now Database Connected And Back to Online')
                print(f'{db_error_tag} RollBack Success : Now Database Connected And Back to Online')
            
            except:
                #line_notify(f'{db_error_tag} Database Still Disconnected | Connection testing will start agin in 5 second')
                print(f'{db_error_tag} Database Still Disconnected | Connection testing will start agin in 5 second')
                time.sleep(5)
            finally:
                session.close()
        
        if db_test == 'SUCCESS' :
            #line_notify(f'{db_error_tag} Database RollBack : SUCCESS')
            print(f'{db_error_tag} Database RollBack : ', db_test)