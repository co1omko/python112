# Функуторы - это объекты клвссов которые можно выполнить как функции

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумет должен быть строкой")
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("?:!.; ")
# print(s1(" Hello World! "))
# print(s1("?:Hello World.;"))

# def strip_chars(char):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумет должен быть строкой")
#         return string.strip(char)
#
#     return wrap
#
#
# s1 = strip_chars("?:!.; ")
# print(s1(" Hello World! "))


# class Person:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     @property
#     def data(self):
#         return self.surname, self.name, self.age
#
#
# class SortKey:
#     def __init__(self, *args):
#         self.__method = args
#
#     def __call__(self, lst):
#         lst.sort(key=lambda i: [i.__dict__[key] for key in self.__method])
#
#
# p = [Person('Иванов', 'Игорь', 28),
#      Person('Петров', 'Степан', 21),
#      Person('Сидоров', 'Антон', 25),
#      Person('Петров', 'Анатолий', 11),
#      Person('Иванов', 'Иван', 23),
#      ]
# for i in p:
#     print(i.data)
# print()
# s1 = SortKey('surname')
# s1(p)
# for i in p:
#     print(i.data)
# print()
# s2 = SortKey('surname', 'name')
# s2(p)
# for i in p:
#     print(i.data)
# print()
# s3 = SortKey('surname', 'name', 'age')
# s3(p)
# for i in p:
#     print(i.data)


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('перед вызовом функции')
#         self.func()
#         print('после вызова функции')
#
#
# @MyDecorator
# def func1():
#     print('func')
#
#
# func1()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('перед вызовом функции')
#         res = self.func(*args, **kwargs)
#         print('после вызова функции')
#         return res
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
# print(func1(2, 5))
# print(func2(2, 3, 5))

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = self.func(a, b)
#         return res ** 2
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             print('перед вызовом функции')
#             print(self.name)
#             func(*args, **kwargs)
#             print('после вызова функции')
#
#         return wrap
#
#
# @MyDecorator("test2")
# def add(a, b):
#     print(a * b)
#
#
# add(2, 2)

# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res ** self.name
#
#         return wrap
#
#
# @MyDecorator(3)
# def add(a, b):
#     return a * b
#
#
# print(add(2, 2))


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(5))


# Дескриптор
# __get__()
# __set__()
# __delete__()
# __set_namne__()

# not-data descriptors - только метод __get__
# data descriptors - все или несколько


# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Ivan", "Petrov")
# print(p.name.get())


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person('Ivan', 'Petrov')
# print(p.name)
# print(p.surname)

# class DisOrder:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f"Значение должно быть положительным")
#         instance.__dict__[self.__name] = value
#
#
# class Order:
#     price = DisOrder()
#     quan = DisOrder()
#
#     def __init__(self, name, price, quan):
#         self.name = name
#         self.price = price
#         self.quan = quan
#
#     def sum(self):
#         return self.price * self.quan
#
#
# a = Order('apple', 5, 10)
# print(a.sum())


class Integer:
    @classmethod
    def varify_coord(cls, coord):
        if not isinstance(coord, int):
            raise TypeError(f"Координата {coord} должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.varify_coord(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point3D(1, 2, 3)
print(p1.__dict__)
