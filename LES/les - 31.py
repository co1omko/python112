import sqlite3 as sq


# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     """)
#     # CREATE TABLE IF NOT EXISTS cost(
#     #     name TEXT, tr_in INTEGER, buy INTEGER
#     # );
#     cur.execute("SELECT model, price FROM cars")
#     # print(con.row_factory)
#     # rows = cur.fetchall() # получить все данные по текущему запросу
#     # rows = cur.fetchmany(5)
#     # rows = cur.fetchone()
#     # print(rows)
#
#     for res in cur:
#         print(res['model'], res['price'])

# cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
# last_row_id = cur.lastrowid # id последней записи
# buy_car_id = 2 # автомобиль который купит покупатель
# cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

# cur.executescript("""
# DELETE FROM cars WHERE model LIKE 'B%';
# UPDATE cars SET price = price + 100;
# """)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

# for car in cars:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# con.commit()  # СОХРАНЯЕТ ВСЕ ИЗМЕНЕНИЯ В БАЗЕ ДАННЫХ
# con.close()

# con = None
# try:
#     con = sq.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()

# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, 'wb')as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     """)
#
#     cur.execute("SELECT ava FROM users LIMIT 1")
#     img = cur.fetchone()['ava']
#
#     write_ava('out.png', img)

    # img = read_ava(1)
    # if img:
    #     binary = sq.Binary(img)
    #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))


# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#
#     # with open("sql_dump.sql", "w")as f:
#     #     for sql in con.iterdump():
#     #         f.write(sql)
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)

# data = [("car", "Машина"), ("house", "Дом"), ("tree", "Дерево"), ("clor", "Цвет")]
#
# con = sq.connect(':memory:')
# with con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS dict(
#     eng TEXT,
#     rus TEXT)
#     """)
#     cur.executemany("INSERT INTO dict VALUES(?, ?)", data)
#
#     cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
#     print(cur.fetchall())


