import os
from sqlalchemy import and_, or_, not_, desc, func, distinct, text

from modelsHW.database import DATABASE_NAME, Session
import create_database as db_creator

from modelsHW.products import Product

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    for it in session.query(Product):
        print(it)
    print("*" * 60)
    for it in session.query(Product).filter(and_(Product.id >= 4, Product.name.like('К%'))):
        print(it)
    print("*" * 60)
    for it in session.query(Product).filter(not_(Product.price <= 130), not_(Product.number.like(2))):
        print(it)
    print("*" * 60)
    for it in session.query(Product).filter(Product.number.like(1)):
        print(it)
    print("*" * 60)
    session.add(Product(name='Баклажан', price=125, number=3))
    session.commit()
    print("*" * 60)
    for it in session.query(Product.price).filter(Product.price < 130).distinct():
        print(it)
    print("*" * 60)