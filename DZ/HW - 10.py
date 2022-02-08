# from math import *
#
#
# def p(x, y):
#     return a * b
#
#
# def t(x, y):
#     return (a * b) / 2
#
#
# def k(x):
#     return round(pi * r ** 2, 2)
#
#
# f = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# if f == 1:
#     a = int(input("1 сторона: "))
#     b = int(input("2 сторона: "))
#     s = p(a, b)
#     print("Площадь: ", s)
# elif f == 2:
#     a = int(input("Основание : "))
#     b = int(input("Высота : "))
#     s = t(a, b)
#     print("Площадь: ", s)
# elif f == 3:
#     r = int(input("Радиус : "))
#     s = k(r)
#     print("Площадь: ", s)


a = []
b = []
for i in range(2, 50):
    for j in range(2, i):
        if i % j == 0:
            b.append(i)
    else:
        a.append(i)
print(min(a))
print(max(b))
