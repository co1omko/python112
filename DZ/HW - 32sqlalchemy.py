import os

from modelsHW.database import DATABASE_NAME
import HW32create_databse as db_creator

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
