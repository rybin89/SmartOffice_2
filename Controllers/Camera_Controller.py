from Models.Camera import Camera
from Models.Cabinet import *
class Camera_Controller():



    def get(self):
        return Camera.select().execute()

    # def get_camera_cabinet(self):
    #     # (SELECT Cabinets.name FROM Cabinets WHERE Cabinets.id = Cameras.cabinet_id)
    #     cabinet = Cabinet.select(Cabinet.name).where(Cabinet.id == Camera.cabinet_id).alias('cabinet')

        return Camera.select(Camera.name,Camera.link, cabinet).execute()
        # return Camera.select(Camera.name,Camera.link, cabinet)

    def add(self,name,link,cabinet):

        # запрос на id введённого кабинета
        cabinet_id = Cabinet.select(Cabinet.id).where(Cabinet.name == cabinet)
        # __cabinet = Cabinet(id=cabinet_id)
        camera = Camera(name=name, link=link, cabinet_id=cabinet_id)
        validator_camera = ModelValidator(camera)
        # validator_cabinet = ModelValidator(__cabinet)
        if validator_camera.validate():
            Camera.insert(name=name, link=link, cabinet_id=cabinet_id).execute()
        else:
            print(validator_camera.errors,)



        # сапрос длбавления записи в таблицу Cameras

        print(f"Камера {name} добавлена в кабинет {cabinet}")
