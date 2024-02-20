import peewee
from peewee import *



# MySQLDatabase() - подключает к СУБД по атрибутам
def connect_peewee():

    connect = MySQLDatabase(
        'rybin_Smart_Of',
        user='rybin_adSmartOf',
        password='111111',
        # host='10.11.13.118'
        host='localhost'
    )

    try:
        # проверить поключение переменной connect
        connect.connect()
        # вернули подключение
        return connect
    except peewee.OperationalError as error:
        print('Ошибка базы данных!', error)



