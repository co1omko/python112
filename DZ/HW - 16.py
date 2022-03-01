# Задание 1
# def func_compute(a):
#     def result(b):
#         return a * b
#
#     return result
#
#
# res = func_compute(2)
# print(res(15))
# print(res(20))
# res = func_compute(3)
# print(res(15))
# print(res(20))

# Задание 2
# print((lambda a, b, c: a * b * c)(2, 5, 5))


# Задание 3/4
students = [{'name': 'Jennifer', 'final': 95},
            {'name': 'David', 'final': 92},
            {'name': 'Nikolas', 'final': 98}]
students.sort(key=lambda i: i['name'])
print(students)
students.sort(key=lambda i: i['final'], reverse=True)
print(students)
print(max(students, key=lambda i: i['final']))
print(min(students, key=lambda i: i['final']))

