from Controllers.Camera_Controller import Camera_Controller
from Controllers.Electrical_line_Controller import *
from Controllers.Cabinet_Controller import *

# line = Electrical_line_Controller()
# line.add('207Т')
# camera = Camera_Controller()

cabinet = Cabinet_Controller()
camera = Camera_Controller()
# try:
#
#     print(camera.get_camera_cabinet())
#     for elem in camera.get_camera_cabinet():
#         print(elem.name, elem.link, elem.cabinet)
#
#     camera.add('#1','https://i.ytimg.com/vi/HR86p6NVGbY/maxresdefault.jpg','312Т')
# except peewee.InterfaceError as error:
#     print('Ошибка!', error)
# except peewee.IntegrityError as error:
#     print('Ошибка!', error)

# try:
#     cabinet.add_value('215','1232')
#     # cabinet.add_value('12','123')
#     # for element in cabinet.get():
#     #     print(element.name,element.department)
# except peewee.DataError as error:
#     print('Ошибка!', error)


# for el in camera.get():
#     print(el.name,el.link,el.cabinet_id.name)
# camera.add('№244', 'ссылка', '215Т')
# for el in camera.get():
#     print(el.name,el.link,el.cabinet_id.name)

electric = Electrical_line_Controller()

for el in electric.get():
    print(el.state, el.cabinet_id.name)
electric.add(False,'207Т')
for el in electric.get():
    print(el.state, el.cabinet_id.name)