# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Employee list")
#         print(self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '657'
#
#         def display(self):
#             print("Name:", self.name)
#             print('Id:', self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#             self.id = '007'
#
#         def display(self):
#             print("Name:", self.name)
#             print('Degree:', self.id)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.intern
# d2 = outer.head
# d1.display()
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Class Outer")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('Class Inner')
#
#         class InnerClass:
#
#             def show(self):
#                 print('Inner Class')
#
#
# outer = Outer()
# outer.show()
# inner1 = outer.inner
# inner1.show()
# inner2 = inner1.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i7'
#
#
# comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.OS()
# my_cpu = Computer.CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('Class Base')
#
#     class Inner:
#
#         def display1(self):
#             print('Inner of Base Class')
#
#
# class SubClass(Base):
#     def __init__(self):
#         print('In SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def dispaly2(self):
#             print('Inner of SubClass')
#
#
# a = SubClass()
# a.display()
# # b = a.db
# b = a.Inner()
# b.display1()
# b.display2()


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end="")
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.model = 'HP'
#             self.cpu = 'i7'
#             self.ozu = '16'
#
#         def show(self):
#             print('==> =', self.model, self.cpu, self.ozu)
#
#
# s = Student("Roman")
# s.show()
# s2 = Student('Vladimir')
# s2.show()


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + 'is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + 'is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + 'is barking')
#
#
# d = Dog('Buddy ')
# d.sleep()
# d.play()
# d.bark()


# class A:
#     # def __init__(self):
#     #     print('Инициальзаор класса А')
#     def hi(self):
#         print('A')
#
#
# class AA(A):
#     def hi(self):
#         print('AA')
#
#
# class B(A):
#     # def __init__(self):
#     #     print('Инициальзаор класса B')
#     def hi(self):
#         print('B')
#
#
# class C(AA):
#     # def __init__(self):
#     #     print('Инициальзаор класса C')
#     def hi(self):
#         print('C')
#
#
# class D(B, C):
#     #     def __init__(self):
#     #         C.__init__(self)
#     #         print('Инициальзаор класса D')
#     #         B.__init__(self)
#     def call_hi(self):
#         C.hi(self)
#
#
# d = D()
# d.call_hi()
# print(D.mro())


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y}"
#
#
# class Style:
#     def __init__(self):
#         print("Инициализатор Style")
#
#
# class Pos:
#     def __init__(self):
#         print('Инициализатор Pos')
#         # super().__init__()
#
#
# class Line(Pos, Style):
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         self._color = color
#         self._width = width
#         self._sp = sp
#         self._ep = ep
#         super().__init__()
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()


# Миксины (примеси)

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='lofifile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclass.txt')
#
#
# subclass = MySubClass()
# subclass.display('Эта строка будет отобращаться и записываться в файл')


# class Goods:
#     def __init__(self, name, width, price):
#         super().__init__()
#         print("Инициализатор Goods")
#         self.name = name
#         self.width = width
#         self.price = price
#
#     def pribt_info(self):
#         print(f'{self.name}, {self.width}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Инициализатор MixinLog")
#         self.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар был продан в 00:00 часов')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.pribt_info()
# n.save_sell_log()
# print(NoteBook.mro())


# Перегрузка операторов


class Clock:
    __DAY = 86400 # число секунда в дне 24*60*60

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError('Секунды должны быть числом')

        self.__sec = sec % self.__DAY

    def get_format_time(self):
        s = self.__sec % 60 # секунды
        m = (self.__sec // 60) % 60 # минуты
        h = (self.__sec // 3600) % 24 # часы
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'



    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def get_seconds(self):
        return self.__sec

    def __add__(self, other): # сложение
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд дожен быть типом Clock")
        return Clock(self.__sec + other.get_seconds())



c1 = Clock(100)
c2 = Clock(200)
c3 = c1 + c2
print(c1.get_format_time())
