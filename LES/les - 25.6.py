# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst = MyList()
# lst.append(10)
# lst.append(20)
# print(lst, lst.get_length())

# class MyMetaclass(type):
#     def __new__(mcs, name, base, attr):
#         print("Создание нового объекта", name)
#         return super(MyMetaclass, mcs).__new__(mcs, name, base, attr)
#
#     def __init__(cls, name, base, attr):
#         print("Инициализатор класса", name)
#         super(MyMetaclass, cls).__init__(name, base, attr)
#
#
# class Student(metaclass=MyMetaclass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student("Анна")
# print("Имя студента", stud.get_name())
# print("Тип объекта Student", type(stud))
# print("Тип класса Student", type(Student))

# import geometry.rect
# import geometry.sq
# import geometry.trian

from geometry import rect, sq, trian
#from geometry import *

r1 = rect.Rectangle(1, 2)
r2 = rect.Rectangle(3, 4)
s1 = sq.Square(10)
s2 = sq.Square(20)
t1 = trian.Triangle(1, 2, 3)
t2 = trian.Triangle(4, 5, 6)
shape = [r1, r2, s1, s2, t1, t2]
for g in shape:
    print(g.get_perimetr())


# from car import electrocar
#
#
# def main():
#     e_car = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
#     e_car.show_car()
#     e_car.description_battary()
#
#
# if __name__ == '__main__':
#     main()


# Упаковка данных
# Сериализация
# Десериализация

# marshal (.pyc)
# pickle
# json

# dump () - сохраняет данные в файл
# dumps ()- сохраняет данные в память
# load () - считывает данные из файла
# loads () - считывает данные из памяти

import pickle


# filename = "basket.txt"
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# with open(filename, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, "rb") as fh:
#     shop_list2 = pickle.load(fh)
#
# print(shop_list2)


# class Test:
#     a_number = 35
#     a_string = "Hello"
#     a_list = [1, 2, 3]
#     a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
#     a_tuple = (22, 23)
#
#     def __str__(self):
#         return f"Число: {Test.a_number}\nСтрока: {Test.a_string}\nСписок: {Test.a_list}\n" \
#                f"Словарь: {Test.a_dict}\nКортеж: {Test.a_tuple}"
#
#
# obj = Test()
# my_obj = pickle.dumps(obj)
# print(f"Сериализация в строку:\n{my_obj}\n")
#
# l_obj = pickle.loads(my_obj)
# print(f"Десериализация данных:\n{l_obj}\n")


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'text'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
#
# print(item3.__dict__)
# print(item3)

# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename)
#         self.count = 0
#
#     def read_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#             return f"{self.count}: {line}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename)
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader('hello.txt')
# print(reader.read_line())
# print(reader.read_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.read_line())
