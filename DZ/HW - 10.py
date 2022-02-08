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

# import random as r
#
#
# matrix = [r.randint(1, 15) for i in range(10)]
# print(matrix)
# for j in range(1, i):
for x in range(1, 15):
    a = []
    for n in range(1, x):
        if x % n == 0 and (x == n or n == 1):
            a.append(n)

    print(a)