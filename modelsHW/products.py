from sqlalchemy import Column, Integer, String

from modelsHW.database import Base


class Product(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    price = Column(Integer)

    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number

    def __repr__(self):
        return f"Наименование продукта: {self.name}, Цена: {self.price}, Номер на складе: {self.number}"

