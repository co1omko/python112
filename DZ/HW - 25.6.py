import math
from hwgeometry import rectangle, cylinder, circle

r1 = rectangle.Rectangle(2, 7)
r2 = rectangle.Rectangle(5, 9)
r3 = rectangle.Rectangle(8, 3)
c1 = cylinder.Cylinder(2, 3)
c2 = cylinder.Cylinder(3, 6)
c3 = cylinder.Cylinder(1, 4)
k1 = circle.Circle(8)
k2 = circle.Circle(5)
k3 = circle.Circle(11)
print("Периметр:", r1.get_perimetr())
print("Периметр:", r2.get_perimetr())
print("Периметр:", r3.get_perimetr())
print("Площадь:", r1.get_square())
print("Площадь:", r2.get_square())
print("Площадь:", r3.get_square())
print("Объем цилиндра:", c1.get_volume())
print("Объем цилиндра:", c2.get_volume())
print("Объем цилиндра:", c3.get_volume())
print("Длинна окружности:", k1.get_long())
print("Длинна окружности:", k2.get_long())
print("Длинна окружности:", k3.get_long())
print("Порщадь круга:", k1.get_square())
print("Порщадь круга:", k2.get_square())
print("Порщадь круга:", k3.get_square())
shape1 = [r1, r2, r3]
shape2 = [c1, c2, c3]
shape3 = [k1, k2, k3]


def max_square():
    return max(shape3, key=lambda a: a.get_square())


print('Окружность с наибольшей площадью: Радиус:', max_square())


def min_perimetr():
    return min(shape1, key=lambda a: a.get_perimetr())


print("Прямоугольник с наименьшим периметром: "'Стороны:', min_perimetr())


def sr_volume():
    return round(c1.get_volume() + c2.get_volume() + c3.get_volume() / len(shape2), 2)


print('Средний объем всех цилиндров:', sr_volume())
