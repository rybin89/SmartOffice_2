from Controllers.LampController import *
from Controllers.SectionController import *

lamp = LampController()
section = SectionController()
#
# lamp.print_get()
# print('Section')
# section.print_get()

# print('add Section')
# section.add('218T-1')
# section.print_get()
# print('Add lamp - 2')
# lamp.add_2('218T-1','218Т')
# lamp.add(1,1)
# lamp.print_get()

# lamp.show(1)
# Список словарей
# print('Add many lamps')
# lamps = [
#     {'seсtion_id': 1, 'cabinet_id':1},
#     {'seсtion_id': 1, 'cabinet_id':1},
#     {'seсtion_id': 4, 'cabinet_id':18},
#     {'seсtion_id': 4, 'cabinet_id':18},
# ]
# lamp.add_many(lamps)
# lamp.print_get()

lamp.show(8)
lamp.update_One(8,True)
lamp.show(8)
lamp.update_Two(8,False)
lamp.show(8)

