from dotenv import load_dotenv
import os

load_dotenv()

environment = os.environ.get('ENVIRONMENT')

if environment == 'DEV' :
    MYSQL_HOST=     os.environ.get('DEV_MYSQL_HOST')
    MYSQL_USER=     os.environ.get('DEV_MYSQL_USER')
    MYSQL_PORT=     os.environ.get('DEV_MYSQL_PORT')
    MYSQL_PASSWORD= os.environ.get('DEV_MYSQL_PASSWORD')
    MYSQL_DATABASE= os.environ.get('DEV_MYSQL_DATABASE')


if environment == 'PROD' :
    MYSQL_HOST =     os.environ.get('PROD_MYSQL_HOST')
    MYSQL_USER =     os.environ.get('PROD_MYSQL_USER')
    MYSQL_PORT =     os.environ.get('PROD_MYSQL_PORT')
    MYSQL_PASSWORD = os.environ.get('PROD_MYSQL_PASSWORD')
    MYSQL_DATABASE = os.environ.get('PROD_MYSQL_DATABASE')