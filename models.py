from peewee import Model, SqliteDatabase, CharField, ForeignKeyField, DecimalField, IntegerField

db = SqliteDatabase("betsy.db")

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    adress = CharField()
    billing_info = CharField()

class Tag(BaseModel):
    name = CharField() 

class Product(BaseModel):
    name = CharField()
    description = CharField()
    price_per_unit = DecimalField(decimal_places=2, auto_round=True)
    quantity_in_stock = IntegerField()
    owner = ForeignKeyField(User) 
    tag = ForeignKeyField(Tag)


class Transactie(BaseModel):
    user = ForeignKeyField(User)
    purchased_product_id = ForeignKeyField(Product)
    purchased_quantity = IntegerField()