# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d1 = dict()
# d1['name'] = d.pop('name')
# d1['salary'] = d.pop('salary')
# print(d1)
# print(d)

d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
d['located'] = d.pop('city')
print(d)