# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 3, 5, 'abc'))


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# a = summa(1, 2, 3, 4, 5, 6, 7)
# b = summa(1, 2, 3)
# print(a)
# print(b)

# def func(*a):
#     return {i: i for i in a}
#
#
# print(func(1, 2, 3, 4, ))
# print(func("gray", (2.17), 3.11, -4))


# def func(*a):
#     res = (sum(a) / len(a))
#     d = []
#     for i in a:
#         if i < res:
#             d.append(i)
#     print(res)
#     print(d)
#
#
# func(1, 2, 3, 4, 5, 6, 7, 8, 9)
# func(3, 6, 1, 9, 5)

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1,2,3,'abc'))

# def func(student, *scores):
#     print("Student name: ", student, end=" ")
#     # for score in scores:
#     print(*scores, sep=", ")
#
#
# func("Igor", 100, 95, 88, 92, 99)
# func("Rick", 69, 20, 33)


# def revers_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2 != 0):
#             res.append(revers_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 81, 91, only_odd=True))


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))

# def info(**data):
#     for key, value in data.items():
#         print(key, "is", value)
#     print()
#
#
# info(firstname="Irina", lastname="Saunal", age=22, phone=1124564789)
# info(firstname="Igor", lastname="Wood", email="igor@mail.ru", age=22, phone=1124564789)


# def db(**kwargs):
#     my_dict.update(**kwargs)
#
#
# my_dict = {'one': 'first'}
# print(db(k1=22, k2=31, k3=11, k4=91))
# print(db(name='Bob',age=31, weight=61, eyes_color="gray"))
# print("my_dict =", my_dict)

def func(a, *args, b=False, **kwargs):
    return a, args, b, kwargs
#
#
print(func(1, 2, 3, 4, b=True, x=11, y=12, z=13))


# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5, 6)
# func2(one=123, two=456)


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, 'one': 1, 'two': 2, **y}
# print(z)

# scope - область видимости функции

# name = "Tom" #глобальная переменная
#
#
# def hi():
#     global name
#     name = "Sam" #локальная переменная
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()