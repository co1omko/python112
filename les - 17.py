# players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}]
# res = sorted(players, key=lambda i: i['last name'])
# print(res)
#
# res = sorted(players, key=lambda i: i['raiting'])
# print(res)
#
# res = sorted(players, key=lambda i: i['raiting'], reverse=True)
# print(res)


# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#     1: (lambda: print('Monday')),
#     2: (lambda: print('Tuesday')),
#     3: (lambda: print('Wednesday')),
#     4: (lambda: print('Thursday')),
#     5: (lambda: print('Friday')),
#     6: (lambda: print('Saturday')),
#     7: (lambda: print('Sunday'))
# }
#
# d[2]()


# from math import pi
#
# sqare = {
#     'circle': lambda r: print(pi * r ** 2),
#     'rectangle': lambda a, b: print(a * b),
#     'trapezoid': lambda a, b, h: print((a + b) * h / 2)
# }
#
# sqare['circle'](2)
# sqare['rectangle'](10, 13)
# sqare['trapezoid'](7, 5, 3)


# print((lambda a, b, c: a if (a <= b) and (b <= c) else (b if (b <= a) and (b <= c) else c))(9, 8, 5))


# map(func, interable) цикл который записывается в одну строку

# def mul(t):
#     return t * 2
#
#
# s = [2, 8, 12, -5, -8]
# ls = list(map(mul, s))
# print(ls)

# s = (2, 8, 12, -5, -8)
# print(tuple(map(lambda t: t * 2, (2, 8, 12, -5, -8))))

# s = ['1', '2', '3', '4', '5']
# s1 = (list(map(int, s)))
# print(s1)
# print(type(s1[0]))

# areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.000135]
# res = list(map(round, areas, range(1, 7)))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))


# filter(func, iterable) возвращает данные при каком то условии

# t = ('abcd', 'abc', 'cdef', 'def', 'ghi')
# print(tuple(filter(lambda s: len(s) == 3, t)))

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

from random import randint


# x = [randint(1, 40) for i in range(10)]
# res = (list(filter(lambda s: (s >= 10) and (s <= 20), x)))
# print(x)
# print('[10; 20] = ', res)

# a = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda s: s % 15 == 0, a))
# print(res)
# res = list(filter(lambda s: not s % 15, a))
# print(res)


# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10)))))
# print([x ** 2 for x in range(10) if x % 2 != 0])

# a = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
# print(list(filter(lambda i: i == i[::-1], a)))

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_hello'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

def my_decorator(func):
    def func_wrapper():
        print('Code before')
        func()
        print('Code aftre')

    return func_wrapper

def func_test():
    print("Hello, I am func 'hello'")

test = my_decorator(func_test)
test()