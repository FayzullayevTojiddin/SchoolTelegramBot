from peewee import Model, MySQLDatabase
from config import Config

database = MySQLDatabase(
    Config.database['name'],
    password=Config.database['password'],
    user=Config.database['user'],
    host=Config.database['host'],
    port=Config.database['port']
)



class BaseModel(Model):
    class Meta:
        database = database