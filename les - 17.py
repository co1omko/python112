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

# def my_decorator(func): #дикорирующая функция
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code aftre')
#
#     return func_wrapper
#
#
# @my_decorator # декоратор
# def func_test(): # декарируемая функция
#     print("Hello, I am func 'hello'")
#
#
# func_test()
# test = my_decorator(func_test)
# test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap()
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() +"</i>"
#
#     return wrap
#
#
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызоа функции: ", count)
#
#     return wrap
#
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные: ", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Лаврова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args: ", args)
#         print("kwargs: ", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "Изучают", study, "\n")
#
#
# print_full_name("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")


# def args_decorator(arg1, arg2): #"Игорь", "Нефедов"
#     print("Аргумент: ", arg1, arg2)
#
#     def wrapper(func1):
#         def wrap(func_arg1, func_arg2):
#             print("Аргументы функции: ", func_arg1, func_arg2)
#             func1(func_arg1, func_arg2)
#             return func1(func_arg1, func_arg2)
#
#         return wrap
#
#     return wrapper
#
#
# @args_decorator("Игорь", "Нефедов")
# def func(first, last):
#     print("Меня зовут: ", first, last)
#
#
# func("Ирина", "Лаврова")


# def args_decorator(decorator_text):
#     def wrapper(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#             print()
#
#         return wrap
#
#     return wrapper
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
# @args_decorator(decorator_text="Hi, ")
# def hello(text, t2):
#     print(text, t2)
#
# hello_world("world!")
# hello("Igor", "Irina")


def multiply(a):
    print(a)

    def wrapper(func):
        def wrap(b):
            print(b)
            return a * func(b)

        return wrap

    return wrapper


@multiply(3)
def return_num(num):
    print(num)
    return num


print(return_num(5))

# def typed(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# # @typed(int, int, int)
# # def typed_fn(x, y, z):
# #     return x * y * z
# #
# #
# # @typed(str, str, str)
# # def typed_fn2(x, y, z):
# #     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="hello!"):
#     return (x + y) * z
#
#
# # print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Hello"))
# #print(typed_fn2("Hello, ", "world, ", "!"))
# print(typed_fn3("Hello, ", "world, ", z=2))


# def decor(tx=None, dec_text=""):
#     def wrapper(func):
#         def wrap(*args):
#             print(dec_text, end="")
#             func(*args)
#
#         return wrap
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# hello_world2("hi!")
#
#
# @decor(dec_text="hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world("world!")

# print(bin(18))
# print(oct(18))
# print(hex(18))


# s = 'abcdefgh'
#
# print(s[slice(2, 5)])
# print(s[slice(5, None, -1)])
# print(s[slice(None, None, -1)])


# s = "python"
# s = s[:3] + 't' + s[4:]
# print(id(s))
# print(s)

# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык програмирования.'
# str2 = change_char_to_str(str1, 'N', 'P')
# print("str1 = ", str1)
# print("str2 = ", str2)
