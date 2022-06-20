import sqlite3 as sq

phone = [
    ('Samsung', 'Galaxy S22', 110000),
    ('Samsung', 'Galaxy S22+', 120000),
    ('Samsung', 'Galaxy S22 Ultra', 150000),
    ('Samsung', 'Galaxy S21', 110000),
    ('Xiaomi', '12 Pro', 140000),
    ('Xiaomi', '12', 80000),
    ('Xiaomi', 'Redmi Note 11 Pro', 30000),
    ('Xiaomi', 'Redmi 10', 15000),
    ('Xiaomi', 'Redmi 9C NFC ', 10000),
]

with sq.connect('phone.db') as con:
    cur = con.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS phone(
        phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
        producer TEXT,
        model TEXT,
        price INTEGER)
    """)
    for ph in phone:
        cur.execute("INSERT INTO phone VALUES(NULL, ?, ?, ?)", ph)
    # cur.execute("INSERT INTO phone VALUES(1, 'Apple', 'iPhone 13 pro MAX', 100000)")
    # cur.execute("INSERT INTO phone VALUES(2, 'Apple', 'iPhone 13 pro', 85000)")
    # cur.execute("INSERT INTO phone VALUES(3, 'Apple', 'iPhone 13', 65000)")
    # cur.execute("INSERT INTO phone VALUES(4, 'Apple', 'iPhone 13 mini', 55000)")
    # cur.execute("INSERT INTO phone VALUES(5, 'Apple', 'iPhone 12 pro', 80000)")
    # cur.execute("INSERT INTO phone VALUES(6, 'Apple', 'iPhone 12', 55000)")
    # cur.execute("INSERT INTO phone VALUES(7, 'Apple', 'iPhone 11 pro', 75000)")
    # cur.execute("INSERT INTO phone VALUES(8, 'Apple', 'iPhone 11', 50000)")
