import math


# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     # def set_x(self, x):  # установить
#     #     self.__x = x
#     #
#     # def get_x(self):  # получить
#     #     return self.__x
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами!")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
# p1 = Point(5, 10)
# # p1.set_x(100)
# # print(p1.get_x())
# # p1.set_coords(50, 70)
# print(p1.get_coords())
# # p1.__x = 100
# # p1.y = 'abc'
# # print(p1.x, p1.y)
# print(p1.__dict__)
# p1._Point__x = 111
# print(p1.__dict__)


#
#
# class Rectangle:
#     def __init__(self, a, b):
#         self.__a = self.__b = 0
#         if Rectangle.__check_value(a) and Rectangle.__check_value(b):
#             self.__a = a
#             self.__b = b
#
#     def __check_value(z):
#         if isinstance(z, (int, float)):
#             return True
#         return False
#
#     def set_a(self, a):
#         if Rectangle.__check_value(a):
#             self.__a = a
#
#     def set_b(self, b):
#         if Rectangle.__check_value(b):
#             self.__b = b
#
#     def get_a(self):
#         return self.__a
#
#     def get_b(self):
#         return self.__b
#
#     def area(self):
#         return self.__a * self.__b
#
#     def perimetr(self):
#         return 2 * (self.__a + self.__b)
#
#     def gipp(self):
#         return math.sqrt(self.__a ** 2 + self.__b ** 2)
#
#     def print_area(self):
#         # for i in range(self.__a):
#         #     print('*' * self.__b)
#         print(('*' * self.__b +'\n') * self.__a)
# r1 = Rectangle(3, 4)
# x = int(input("Высота: "))
# y = int(input("Ширина: "))
# r1.set_a(x)
# r1.set_b(y)
# print(r1.get_b(), r1.get_a())
# print(r1.area())
# print(r1.perimetr())
# print(round(r1.gipp(), 2))
# r1.print_area()


# class Point:
#     WIDTH = 5
#     __slots__ = ["__x", "__y"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     # def set_x(self, x):  # установить
#     #     self.__x = x
#     #
#     # def get_x(self):  # получить
#     #     return self.__x
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами!")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def __getattr__(self, item):
#         return f"В классе {__class__.__name__} отсутствует атрибут: {item}"
#
#     def __getattribute__(self, item):
#         if item == "_Point__x":
#             return "Закрытая переменная"
#         else:
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == "WIDTH":
#             raise AttributeError("Нельзя изменять значение WIDTH")
#         else:
#             self.__dict__[key] = value
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# # p1.zzz = 12
# # print(p1.zzz)
# # p1.set_coords(45, 20)
# # print(p1._Point__x)
# # print(p1.get_coords())
# # print(p1.__dict__)
# # p1.WIDTH = 7


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("Сеттер")
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     def __get_x(self):
#         print("Геттер")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coordX = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.coordX = 100.0
# print(p1.coordX)
# print(p1.__dict__)
# del p1.coordX


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         print("Геттер")
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         print("Сеттер")
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # coordX = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100.0
# print(p1.x)
# del p1.x
# print(p1.__dict__)


class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @name.deleter
    def name(self):
        del self.__name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, o):
        self.__old = o

    @old.deleter
    def old(self):
        del self.__old

p1 = Person("Irina", 26)
print(p1.__dict__)
p1.old = 31
print(p1.old)
# del p1.old
p1.name = "Igor"
print(p1.name)
# del p1.name
print(p1.__dict__)
