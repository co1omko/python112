players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
           {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
           {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
           {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}]
res = sorted(players, key=lambda i: i['last name'])
print(res)

res = sorted(players, key=lambda i: i['raiting'])
print(res)

res = sorted(players, key=lambda i: i['raiting'], reverse=True)
print(res)