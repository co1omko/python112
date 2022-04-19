from abc import ABC, abstractmethod
import math


class Root(ABC):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class Linear(Root):

    def equations(self):
        if self.a != 0:
            print(round(self.b / self.a, 2))
        elif self.a == 0 and self.b == 0:
            print("Бесконечное количесво решений")
        else:
            print("Решений нет")


class Square(Root):
    def equations(self):
        disc = self.b ** 2 - 4 * self.a * self.c
        print(disc)
        if disc > 0:
            x1 = (-self.b + math.sqrt(disc)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(disc)) / (2 * self.a)
            print("x1 = %.2f\nx2 = %.2f" % (x1, x2))
        elif disc == 0:
            x = -self.b / (2 * self.a)
            print("x = %.2f" % x)
        else:
            print("Корней нет")



l = Linear(3, 7, 0)
print(l.equations())
l = Square(1, 4, 3)
print()
print(l.equations())