from models import (db, User, Tag, Product, Transactie)
import os

def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsy.db")
    if os.path.exists(database_path):
        os.remove(database_path)

def populate_test_data():
    db.connect()

    db.create_tables(
        [
            User,
            Tag,
            Product,
            Transactie
        ]
    )

    users = [["Ruud", "Dick Ketstraat", "Credit Card"], ["Guus", "Sluislaan", "PayPal"], ["Bram", "Fonteinkruid", "iDeal"]]
    tags = ["wol", "gebreid", "spijkerbroek", "slim-fit", "cap"]
    products = [["Trui","Gebreide wollen trui",  50, 2, 1, 1], ["Broek", "Stoere spijkerbroek, slim-fit", 80, 3, 2, 3],["Pet", "Baseball cap met zonneklep", 10, 1, 3, 5]]
    transactions = [[2, 1, 1],[2,3,2]]

    for user in users:
        User.create(name = user[0], adress = user[1], billing_info = user[2])

    for tag in tags:
        Tag.create(name = tag)

    for product in products:
        Product.create(name = product[0], description = product[1], price_per_unit = product[2], quantity_in_stock = product[3], owner = product[4], tag = product[5])

    for transaction in transactions:
        Transactie.create(user = transaction[0], purchased_product_id = transaction[1], purchased_quantity = transaction[2])    

    db.close()    