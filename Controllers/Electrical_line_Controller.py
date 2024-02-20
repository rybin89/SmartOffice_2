from Models.Electrical_line import *

class Electrical_line_Controller():

    def add(self,state,cabinet):
        # переменной cabinet_id передаётся результат запроса в класс Cabinet? который выводит id

        # electric = Electrical_line(cabinet_id = cabinet)


        cabinet_id = Cabinet.select(Cabinet.id).where(Cabinet.name == cabinet)

        __el = Electrical_line(state, cabinet_id)
        validator = ModelValidator(__el)
        validator.validate()
        Electrical_line.insert(state = state, cabinet_id = cabinet_id).execute()
    def get(self):
        return Electrical_line.select().execute()