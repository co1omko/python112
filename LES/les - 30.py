# Сокет - это программный интерфейс для обеспечения информационного обменя между процессами

# Сокет состоит из IP - адреса и порта.

# 127.0.0.1:5000

# import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()  # получим список из элементов которые разделятся пробелами
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found<h3>'
#     elif code == 405:
#         return '<h1>405</h1><h3>Method Allowed<h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     header, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (header + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()  # 127.0.0.1:5000
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#
#
# if __name__ == '__main__':
#     run()


import sqlite3 as sq

# con = sq.connect('profile.db')
# cur = con.cursor()
#
# cur.execute("""
# """)
# con.close()

# with sq.connect('profile.db') as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE users")


    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # sum REAL,
    # date TEXT
    # )""")


# with sq.connect('user.db') as con:
#     cur = con.cursor()
#
#     cur.execute("""
#        DROP TABLE person_table
#        """)
    # cur.execute("""
    # ALTER TABLE person_table
    # DROP COLUMN home_address;
    # """)
    # cur.execute("""
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address;
    # """)

    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address;
    # """)

    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT +79090000000,
    # age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )""")
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)

with sq.connect('db_4.db') as con:
    cur = con.cursor()
    cur.execute("""
        SELECT * 
        FROM Ware
        ORDER BY Price DESC
        LIMIT 2, 5;
        """)

    # res = cur.fetchall()
    # print(res)
    # for res in cur:
    #     print(res)
    res = cur.fetchone()
    res2 = cur.fetchmany(2)
    print(res)
    print(res2)