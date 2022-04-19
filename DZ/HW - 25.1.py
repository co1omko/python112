import math


class Pair:
    def __init__(self, num_a, num_b):
        self.__num_a = num_a
        self.__num_b = num_b

    @property
    def num_a(self):
        return self.__num_a

    @num_a.setter
    def num_a(self, a):
        self.__num_a = a

    @property
    def num_b(self):
        return self.__num_b

    @num_b.setter
    def num_b(self, b):
        self.__num_b = b

    def summa(self):
        return self.__num_a + self.__num_b

    def prod(self):
        return self.__num_a * self.__num_b


class RightTriangle(Pair):
    def __init__(self, num_a, num_b):
        super().__init__(num_a, num_b)

    def gip(self):
        c = self.num_a ** 2 + self.num_b ** 2
        return round(math.sqrt(c), 2)

    def area(self):
        return self.num_a * self.num_b / 2


r = RightTriangle(5, 8)
print("Гипотенуза ABC:", r.gip())
print(f"Прямоугольный треугольник ABC ({r.num_a}, {r.num_b}, {r.gip()})")
print("Площадь ABC:", r.area())
print()
print("Сумма:", r.summa())
print("Произведение:", r.prod())
print()
r.num_a = 10
print("Гипотенуза ABC:", r.gip())
r.num_b = 20
print("Гипотенуза ABC:", r.gip())
print("Сумма:", r.summa())
print("Произведение:", r.prod())
print("Площадь ABC:", r.area())
