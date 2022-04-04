# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.x = 100
# p1.y = 300
# p1.set_coords(5, 10)
# # Point.set_coords(p1, "Elena")
#
# p2 = Point()
# p2.set_coords(3, 8)
# print(p2.__dict__)

# print(type(p1))
# print(isinstance(p1, Point))
# print(p1.x, p1.y)
# print(p1.__dict__)
# print(getattr(p1, "x"))
# print(getattr(p1, "z", "No"))
# print(hasattr(p1, "z"))
# print(hasattr(p1, "y"))
# print(setattr(p1, "z", 7)) # добавить атрибут
# print(p1.__dict__)
# delattr(p1, "z")# удаление атрибута
# print(p1.__dict__)
# p2 = Point()
# print(p2.x, p2.y)
# print(p2.__dict__)
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}\nГород: {self.city}\nАдрес: {self.address}")
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def self_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "ЧИстопрудный бульвар, 1А")
# h1.print_info()
# h1.self_name("Егор")
# print(h1.get_name())

# class Auto:
#     model = "model"
#     year = "0000"
#     prod = "prod"
#     power = "power"
#     color = "color"
#     price = "price"
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(
#             f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.prod}\nМощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
#         print('=' * 40)
#
#     def input_info(self, first_model, year, prod, power, color, price):
#         self.model = first_model
#         self.year = year
#         self.prod = prod
#         self.power = power
#         self.color = color
#         self.price = price
#
#     def set_power(self, power):
#         self.power = power
#
#     def get_power(self):
#         return self.power
#
#
# h1 = Auto()
# h1.input_info("X7 M50i", "2021", "BMW", "530 л.с.", "write", "10790000")
# h1.print_info()
# h1.set_power("550")
# print(h1.get_power())


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Данные сотрудника: ", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника: ", self.skill, "\n")
#
#
# p1 = Person("Viktor", 'Reznik')
# p1.print_info()
# p1.add_skill(3)
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)


# class Point:
#
#     # def __new__(cls, *args, **kwargs):
#     #     print("Constructor")
#     #     return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print("Initializator")
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удалить экземпляр: " + self.__class__.__name__)
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p2 = Point()
# print(p2.__dict__)

# class Point:
#     count = 0  # статическое свойство
#
#     def __init__(self, x=0, y=0):
#         self.x = x  # динамические свойсва
#         self.y = y
#         Point.count += 1
#         # self.count += 1
#
#
# p1 = Point(5, 10)
#
# p2 = Point(10, 20)
#
# p3 = Point(1, 8)
# print(Point.count)
# print(p1.count)
# print(p2.count)


class Robot:
    k = 0

    def __init__(self, name):
        self.name = name
        print("Инициализация робота: ", self.name)
        print("Приветствую! Меня зовут: ", self.name)
        Robot.k += 1

    def __del__(self):
        print(self.name, "выключсется!")
        Robot.k -= 1

        if Robot.k == 0:
            print(self.name, "был последним")
        else:
            print("Работающий роботов: ", Robot.k)


droid1 = Robot("R2-D2")
print("Численность роботов: ", Robot.k)

droid2 = Robot("S-3PO")
print("Численность роботов: ", Robot.k)

droid3 = Robot("SC-RO")
print("Численность роботов: ", Robot.k)

droid4 = Robot("YY-XX")
print("Численность роботов: ", Robot.k)

print("*" * 20)
del droid1
del droid2
del droid3
del droid4
print("Численность роботов: ", Robot.k)