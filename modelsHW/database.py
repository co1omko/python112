from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'products.db'

engine = create_engine(f'splite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
