from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from variables.variable import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE

db_user     = MYSQL_USER
db_passwd   = MYSQL_PASSWORD
db_host     = MYSQL_HOST
db_port     = MYSQL_PORT
db_name     = MYSQL_DATABASE

db_connect = f"mysql+pymysql://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}"

engine = create_engine(db_connect,pool_pre_ping=True,pool_recycle=3600)

#Create Session
Session = sessionmaker(bind=engine)
session = Session()
#=======================