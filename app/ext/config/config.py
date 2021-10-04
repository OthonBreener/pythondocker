from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:

    def __init__(self):
        self.__connection_string = 'mysql+pymysql://root:senha@mysqldb/teste' 
