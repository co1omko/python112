# class Point:
#     __count = 0  # статическое свойство
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 4)
# p2 = Point()
# p3 = Point()
# print(Point.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Point:
#
#     @staticmethod
#     def max(a, b, c, d):
#         if a > b > c > d:
#             return a
#         elif b > a > c > d:
#             return b
#         elif c > a > b > d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a < b < c < d:
#             return a
#         elif b < a < c < d:
#             return b
#         elif c < a < b < d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def average(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factor(x):
#         c = 1
#         for i in range(1, x + 1):
#             c *= i
#         return c
#
#
# print(Point.max(6, 7, 3, 2))
# print(Point.min(6, 7, 3, 2))
# print(Point.average(6, 7, 3, 2))
# print(Point.factor(9))


# class Temperatur:
#     count = 0
#
#     @staticmethod
#     def faringeit(x):
#         Temperatur.count += 1
#         return x * 1.8 + 32
#
#     @staticmethod
#     def cals(x):
#         Temperatur.count += 1
#         return (x - 32) / 1.8
#
#
# print(Temperatur.faringeit(15))
# print(Temperatur.faringeit(30))
# print(Temperatur.cals(59))
# print(Temperatur.count)


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_validate(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '01.01.2020',
#     '21.31.2020'
# ]
#
# for string_date in dates:
#     if Date.is_date_validate(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print("Неправельный формат даты")

# date = Date.from_string("23.10.2021")
# print(date.string_to_db())
# date = Date.from_string("21.10.2021")
# print(date.string_to_db())


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value  # баланс счета
        print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}')

    def edit_owner(self, surname):
        self.surname = surname

    def add_percents(self):
        self.value += self.value * self.percent
        print('Проценты были успешно начислены')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"Недостаточно средств на счете {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} Было успешно снято")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} Было успешно зачислено!")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий баланс: {self.value} {Account.suffix}")


    def print_info(self):
        print("Информация о счете:")
        print('-' * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print('-' * 20)


acc = Account('123456', 'Долгих', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()
acc.edit_owner('Дюма')
acc.print_info()
print()
acc.add_percents()
print()
acc.withdraw_money(3000)
acc.withdraw_money(100)
print()
acc.add_money(5000)
acc.withdraw_money(3000)


