import math


class Square:
    count = 0

    @staticmethod
    def heron(a, b, c):
        Square.count += 1
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def triangle(b, h):
        Square.count += 1
        return b * h / 2

    @staticmethod
    def square(a):
        Square.count += 1
        return a * a

    @staticmethod
    def rectangle(a, b):
        Square.count += 1
        return a * b


s = Square
print("Площадь треугольника по формуле Герона", s.heron(3, 4, 5))
print("Площадь треугольника через оснвание и высоту", s.triangle(6, 7))
print("Площадь квадрата", s.square(7))
print("Площадь прямоугольника", s.rectangle(2, 6))
print("Количество подсчетов площади:", s.count)
