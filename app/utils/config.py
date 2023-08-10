from urllib.parse import quote_plus
import os


class BaseConfig:
    def __init__(self):
        self.user = os.getenv('USER')
        self.password = os.getenv('PASSWORD')
        self.encoded_password = quote_plus(self.password)
        self.host = 'localhost'
        self.port = '3306'
        self.database = 'testdb'
        self.SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{self.user}:{self.encoded_password}@{self.host}:3306/{self.database}"
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False

