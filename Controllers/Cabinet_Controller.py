from Controllers.Controller import Controller
from Models.Cabinet import *
from Validators.BaseValidator import BaseValidator


# from peewee_validates import *

# котроллер для таблицы Cabinets, в которой будут созданы запросы в виде функций

class Cabinet_Controller(BaseValidator):



#     фунцции и методы описывающие действия над записями таблицы (запросы)
#     def __int__(self):
#         self.__table = Cabinet
#

    # Добавить запись
    def add_value(self,name,departament):
        cabinet = Cabinet(name = name, department = departament)
        validator = ModelValidator(cabinet)
        if validator.validate():
            Cabinet.insert(name=name, department=departament).execute()
        else:
            print('Ошибка',validator.errors)
        #

    def get(self):
        return Cabinet.select().execute()
    def show(self, name):
        return Cabinet.select(Cabinet.name, Cabinet.department).where(Cabinet.name == name).execute()
    # ОБНОВЛЕНИЯ ИМЕНИ по id

    def update_name(self,new_name, id):
        Cabinet.update({Cabinet.name:new_name}).where(Cabinet.id == id).execute()

    # удаление
    def delete_field(self,id):
        Cabinet.delete().where(Cabinet.id == id).execute()
    class Meta:

        messages = {
            'name.required': 'Введите имя',
            'required': 'Введите значение',
            'unique': 'Значение должно быть уникальным',

        }