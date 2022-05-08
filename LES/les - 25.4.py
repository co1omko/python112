# class Clock:
#     __DAY = 86400  # число секунда в дне 24*60*60
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError('Секунды должны быть числом')
#
#         self.__sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.__sec % 60  # секунды
#         m = (self.__sec // 60) % 60  # минуты
#         h = (self.__sec // 3600) % 24  # часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def get_seconds(self):
#         return self.__sec
#
#     # def __add__(self, other):  # сложение
#     #     if not isinstance(other, Clock):
#     #         raise ArithmeticError("Правый операнд дожен быть типом Clock")
#     #     return Clock(self.__sec + other.get_seconds())
#
#     # def __iadd__(self, other):
#     #     if not isinstance(other, Clock):
#     #         raise ArithmeticError("Правый операнд дожен быть типом Clock")
#     #     self.__sec += other.get_seconds()
#     #     return self
#
#     # def __eq__(self, other):
#     #     return self.__sec == other.get_seconds()
#     #
#     # def __ne__(self, other):
#     #     return not self.__eq__(other)
#
#     def __gt__(self, other):
#         return self.__sec > other.get_seconds()
#
#     def __ge__(self, other):
#         return self.__sec >= other.get_seconds()
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Ключ должен быть строкой')
#
#         if item == 'hour':
#             return (self.__sec // 3600) % 24
#         elif item == 'min':
#             return (self.__sec // 60) % 60
#         elif item == 'sec':
#             return self.__sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError('Ключ должен быть строкой')
#         if not isinstance(value, int):
#             raise ValueError('Значение должно быть целым числом')
#         h = (self.__sec // 3600) % 24
#         m = (self.__sec // 60) % 60
#         s = self.__sec % 60
#         if key == 'hour':
#             self.__sec = s + 60 * m + value * 3600
#         elif key == 'min':
#             self.__sec = s + 60 * value + h * 3600
#         elif key == 'sec':
#             self.__sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1['hour'] = 10
# c1['min'] = 26
# c1['sec'] = 59
# print(c1['hour'], c1['min'], c1['sec'])
# c1 = Clock(100)
# c2 = Clock(200)
# c4 = Clock(300)
# print(c1.get_format_time())
# print(c2.get_format_time())
# print('c2 > c1', c2 > c1)
# print('c2 >= c1', c2 >= c1)
# print('c2 > c1', c2 < c1)
# print('c2 >= c1', c2 <= c1)
# # if c1 == c2:
# #     print("Вредям одинаково")
# # if c1 != c2:
# #     print("Время разное")
# # c4 += c2
# # print(c1.get_format_time())
# # print(c3.get_format_time())
# # print(c4.get_format_time())


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#         # if key >= len(self.marks):
#         #     raise TypeError("Такого индекса не существует")
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError('Индекс должен быть целым числом')
#         del self.marks[key]
#
# s1 = Student('Сергей', [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# print(s1[2])
# del s1[2]
# print(s1.marks)


# полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))
# print(t2.total(35))


# class Cat:
#     def __init__(self, animal, name, age):
#         self.animal = animal
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я {self.animal}. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def sound(self):
#         return f"{self.name} мяукает"
#
#
# class Dog:
#     def __init__(self, animal, name, age):
#         self.animal = animal
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я {self.animal}. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def sound(self):
#         return f"{self.name} гавкает"
#
#
# c1 = Cat("кот", "Пушок", 2.5)
# d1 = Dog("собака", "Мухтар", 4)
# for i in (c1, d1):
#     print(i.info())
#     print(i.sound())


# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def info(self):
#         print(f"{self.surname} {self.name} {self.age}")
#
#
# class Student(Human):
#     def __init__(self, spec, group, reit, name, surname, age):
#         super().__init__(name, surname, age)
#         self.spec = spec
#         self.group = group
#         self.reit = reit
#
#     def info(self):
#         print(f"{self.spec} {self.group} {self.reit}", end=" ")
#         super().info()
#
#
# class Teacher(Human):
#     def __init__(self, spec, exp, name, surname, age):
#         super().__init__(name, surname, age)
#         self.spec = spec
#         self.exp = exp
#
#     def info(self):
#         print(f"{self.spec} {self.exp}", end=" ")
#         super().info()
#
#
# class Graduate(Student):
#     def __init__(self, topic, name, surname, age, spec, group, reit):
#         super().__init__(name, surname, age, spec, group, reit)
#         self.topic = topic
#
#     def info(self):
#         print(f"{self.topic}", end=" ")
#         super().info()
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f"{self.name}"
# cat = Cat('Пушок')
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#
# p = Point(1, 2, 7)
# print(len(p))

# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(2, 8)
# print(p1.length)


# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print('pt =', pt.__sizeof__())
# print('pt2 =', pt2.__sizeof__() + pt2.__dict__.__sizeof__())


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point):
    __slots__ = 'z'

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


pt = Point(1, 2)
pt3 = Point3D(10, 20, 30)
print(pt3.x, pt3.y, pt3.z)
# print(pt3.__dict__)