from Models.Lamp import *

class LampController():

    def get(self):
        return Lamp.select()

    def print_get(self):
        for fields in self.get():
            print(fields.state, fields.seсtion_id.name,fields.cabinet_id.name,fields.cabinet_id.department)

    # вывод одной записи (строки) из таблицы

    def show(self, arg_id):
        query = Lamp.get(Lamp.id == arg_id)
        print('Состояние лампы',query.state,'Имя секции',query.seсtion_id.name,'Кабинет:', query.cabinet_id.name)

    # Добавить по id Кабинета и Секции
    def add(self,section,cabinet):
        Lamp.create(seсtion_id = section, cabinet_id = cabinet)

    # Добавить по name Кабинета и Секции

    def add_2(self,section, cabinet):
        section_id = Section.get(Section.name == section).id
        cabinet_id = Cabinet.get(Cabinet.name == cabinet).id

        Lamp.create(seсtion_id=section_id,cabinet_id=cabinet_id)
        print('Лампа добавлена')

    # Добавить несколько записей
    def add_many(self,data):
        Lamp.insert_many(data).execute()

    # Обновление пособ №1 save()
    def update_One(self,arg_id, arg_state):
        lamp = Lamp.get(Lamp.id==arg_id) #создание из выбранной записи по id объекта
        lamp.state = arg_state #изменяем у выбранного объекта занчение состояния
        lamp.save() # c помощью функции save() обновляем запись

    # Обновление пособ №2 update()

    def update_Two(self,arg_id,arg_state):
        Lamp.update(state = arg_state).where(Lamp.id == arg_id).execute()