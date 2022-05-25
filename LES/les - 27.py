# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# # print(todos[:10])
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
#
# max_users = " and ".join(users)
# s = 's' if len(users) > 1 else ''
# print(f"user{s} {max_users} completed {max_complete} TODOs")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_data_file.json', 'w') as data_file:
#     filter_todos = list(filter(keep, todos))
#
#     json.dump(filter_todos, data_file, indent=2)


# CSV(Comma Separated Values)

import csv

# with open('data.csv') as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")
#     count = 0
#
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#
#     print(f"Всего в файле {count} строк.")


with open('data.csv') as r_file:
    fieldnames = ['Имя', 'Профессия', 'Год рождения']
    file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=fieldnames)
    count = 0

    for row in file_reader:
        if count == 0:
            print(f"Файл содержит столбцы: {', '.join(row)}")
        print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
        count += 1

    print(f"Всего в файле {count} строк.")


# with open("student.csv", mode='w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(['Женя', '9', '15'])
#     writer.writerow(['Саша', '5', '12'])
#     writer.writerow(['Маша', '11', '18'])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data_new.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
       # writer.writerows(data)
#
# with open('sw_data_new.csv') as f:
#     print(f.read())


# with open('student1.csv', 'w') as f:
#     names = ['Имя', 'Возраст']
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({'Имя': 'Саша', 'Возраст': '6'})
#     file_writer.writerow({'Имя': 'Маша', 'Возраст': '15'})
#     file_writer.writerow({'Имя': 'Вова', 'Возраст': '14'})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dictwriter.csv', 'w') as f:
#     write = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     write.writeheader()
#     for d in data:
#         write.writerow(d)


# from bs4 import BeautifulSoup
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# # row = soup.find("div", class_="name").text
# # row = soup.find("div", class_='name')
# row = soup.find_all("div", {'class': 'name'})
# # row = soup.find_all("div", class_="row")[1].find_all("div", class_='links')
# print(row)
