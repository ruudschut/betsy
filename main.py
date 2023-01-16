__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import db, User, Tag, Product, Transactie
from peewee import JOIN

def search(term):
    query = (
        Product.select()
        .where(Product.name.contains(term)|Product.description.contains(term))
        )
    for item in query:
        print(item.name)

def print_product_names():
    for pd in Product.select():
        print(pd.name)

def list_user_products(user_id):
    query = (
        Product.select(Product, User)
        .join(User)
        .where(Product.owner == user_id)
    )
    for item in query:
        print(item.name)


def list_products_per_tag(tag_id):
    query = (
        Product.select(Product, Tag)
        .join(Tag)
        .where(Tag.name == tag_id)
    )
    for item in query:
        print(item.name)


def add_product_to_catalog(user_id, product):
    Product.create(name = product[0], description = product[1], price_per_unit = product[2], quantity_in_stock = product[3], owner = user_id, tag = product[4])


def update_stock(product_id, new_quantity):
    query = (
        Product.update(quantity_in_stock= new_quantity)
        .where(Product.id == product_id)
        )
    query.execute()    

def purchase_product(product_id, buyer_id, quantity):
    Transactie.create(user= buyer_id, purchased_product_id= product_id, purchased_quantity = quantity)
    query = (
        Product.update(quantity_in_stock= (Product.quantity_in_stock - quantity))
        .where(Product.id == product_id)
    )
    query.execute()



def remove_product(product_id):
    query = (
        Product.delete()
        .where(Product.id == product_id)
    )
    query.execute()