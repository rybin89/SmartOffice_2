from Models.Air_conditioners import *

class Air_conditioners_Controller():

    # Добавить запись
    def add_value(self,name,state,cabinet):
        cabinet_id = Cabinet.select(Cabinet.id).where(Cabinet.name == cabinet)
        Air_conditioners.insert(name = name, state = state, cabinet_id = cabinet_id).execute()

    def get(self):
        return Air_conditioners.select().execute()

    def show(self, name):
        return Air_conditioners.select(Air_conditioners.name, Air_conditioners.department).where(Air_conditioners.name == name).execute()
    # ОБНОВЛЕНИЯ ИМЕНИ по id

    def update_name(self,new_name, id):
        Air_conditioners.update({Air_conditioners.name:new_name}).where(Air_conditioners.id == id).execute()

    # удаление
    def delete_field(self,id):
        Air_conditioners.delete().where(Air_conditioners.id == id).execute()