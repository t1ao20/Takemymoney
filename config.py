import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:tsao0120@127.0.0.1:3306/takemymoney-db'
'
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
