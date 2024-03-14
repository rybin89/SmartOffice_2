from Controllers.Controller import Controller
from Models.Cabinet import *



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
        return Cabinet.get(Cabinet.name == name)
        # return Cabinet.select(Cabinet.name, Cabinet.department).where(Cabinet.name == name).execute()
    def show_id(self,name):
        return Cabinet.get(Cabinet.name == name).id
    # Метод вывода последней записи
    def last_row(self):

        return Cabinet.select().order_by(Cabinet.id.desc()).limit(1)


    # ОБНОВЛЕНИЯ ИМЕНИ по id

    def update_name(self,new_name, old_name):
        cabinet = Cabinet(name=new_name,department='departament')

        validator = ModelValidator(cabinet)
        if validator.validate():
            Cabinet.update({Cabinet.name:new_name}).where(Cabinet.name == old_name).execute()
        else:
            print('Ошибка',validator.errors)

    # удаление
    def delete_field(self,name):
        cabinet = Cabinet(name=name,department='departament')

        validator = ModelValidator(cabinet)
        if validator.validate()!= True:
            Cabinet.delete().where(Cabinet.name == name).execute()
        else:
            print('Ошибка: НЕТ кабинета с таким названием')
    # Метод вывода количесва записей
    def count_row(self):
        return Cabinet.select().count()

    class Meta:

        messages = {
            'name.required': 'Введите имя',
            'required': 'Введите значение',
            'unique': 'Значение должно быть уникальным',

        }
if __name__ == "__main__":

    print(Cabinet_Controller().show_id('218Т'))