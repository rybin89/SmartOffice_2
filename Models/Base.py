import peewee
from peewee_validates import *

from Connection.connection_peewee import *


# Базовая модель

class Base(Model):


    class Meta:
        # подключение к БД
        database = connect_peewee()
        messages = {
            'name.required': 'Введите имя',
            'required': 'Введите значение',
            'unique': 'Значение должно быть уникальным',

        }
