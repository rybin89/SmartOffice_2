import peewee
from peewee import *
import configparser
import os
from Logging.logger_model import *
# Абсолютный путь к файлу конфигурации
path = r'C:\Smart Office\Configuration\config.ini'
absolut_path = os.path.abspath(path)

# подключение к файлу конфигурации
config = configparser.ConfigParser()
config.read(absolut_path,encoding='utf-8')

database = config['DbConnect']['database']
user  = config['DbConnect']['user']
password  = config['DbConnect']['password']
host  = config['DbConnect']['host']
# MySQLDatabase() - подключает к СУБД по атрибутам
def connect_peewee():

    connect = MySQLDatabase(
        database,
        user=user,
        password=password,
        host=host
        # host='localhost'
    )

    try:
        # проверить поключение переменной connect
        connect.connect()

        # вернули подключение
        return connect
    except:
        logging.error("Ошибка", exc_info=True)



