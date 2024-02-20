from Models.Base import *
from Models.Cabinet import *
# Модель описывает сущность(таблицу) БД Air_conditioners

class Air_conditioners(Base):
    # название и тип полей (столбцов)
    id = PrimaryKeyField(unique=True)
    name = CharField(max_length=15,null=False)
    state = BooleanField()
    cabinet_id = ForeignKeyField(Cabinet)

    class Meta:
        table_name = 'Air_conditioners'