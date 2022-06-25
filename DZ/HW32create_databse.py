from faker import Faker
from modelsHW.database import create_db, Session
from modelsHW.products import Product


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    product_name = ['Помидор', 'Огурец', 'Морковь', 'Перец', 'Картофель', 'Капуста']
    for it in enumerate(product_name):
        product = Product(name=it)
        session.add(product)

    faker = Faker('ru-Ru')
    session.commit()

    name = faker.name().split()
    price = faker.random.randint(50, 150)
    number = faker.random.randint(1, 3)
    product = Product(name, price, number)
    session.add(product)

    session.commit()
    session.close()