class Clock:
    __DAY = 86400  # число секунда в дне 24*60*60

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError('Секунды должны быть числом')

        self.__sec = sec % self.__DAY

    def get_format_time(self):
        s = self.__sec % 60  # секунды
        m = (self.__sec // 60) % 60  # минуты
        h = (self.__sec // 3600) % 24  # часы
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def get_seconds(self):
        return self.__sec

    def __sub__(self, other):  # сложение
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд дожен быть типом Clock")
        return Clock(self.__sec - other.get_seconds())

    def __mul__(self, other):  # сложение
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд дожен быть типом Clock")
        return Clock(self.__sec * other.get_seconds())

    def __floordiv__(self, other):  # сложение
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд дожен быть типом Clock")
        return Clock(self.__sec // other.get_seconds())

    def __mod__(self, other):  # сложение
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд дожен быть типом Clock")
        return Clock(self.__sec % other.get_seconds())


c1 = Clock(600)
c2 = Clock(200)
print('c1:', c1.get_format_time())
c3 = c1 - c2
print('c1 - c2:', c3.get_format_time())
c4 = c1 * c2
print('c1 * c2', c4.get_format_time())
c5 = c1 // c2
print('c1 // c2', c5.get_format_time())
c6 = c1 % c2
print('c1 % c2', c6.get_format_time())
c1 -= c2
print('c1 -= c2', c1.get_format_time())
c1 *= c2
print('c1 *= c2', c1.get_format_time())
c1 //= c2
print('c1 = c2', c1.get_format_time())
c1 %= c2
print('c1 -= c2', c1.get_format_time())










