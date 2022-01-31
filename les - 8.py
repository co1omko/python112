import random as r
# b = int(input("Разамер списка: "))
# a = list()
# #for i in range(50):
# while len(a) != b:
#     w = r.randint(1, b)
#     if w not in a:
#         a.extend([w])
# print(a)


# w, h = 5, 4
# #matrix = [[r.randint(1, 30)for x in range(w)]for y in range(h)]
# matrix = []
# for y in range(h):
#     m = []
#     for x in range(w):
#         m.append(r.randint(1, 30))
#     matrix.extend([m])
# print(matrix)
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print()

# w, h = 3, 4
# ch = 0
# matrix = [[r.randint(-20, 10)for x in range(w)]for y in range(h)]
# print(matrix)
# for h in matrix:
#     for w in h:
#         if w < 0:
#             ch += 1
#         print(w, end="\t\t")
#     print()
# print("Количество отричательных элементов: ", ch)


# w, h = 3, 4
# ch = 1
# matrix = [[r.randint(0, 4)for x in range(w)]for y in range(h)]
# print(matrix)
# for h in matrix:
#     for w in h:
#         if w > 0:
#             ch *= w
#         print(w, end="\t\t")
#     print()
# print("Произведение не нулевых элементов: ", ch)

# w, h = 6, 6
# ch = 1
# matrix = [[r.randint(0, 10)for x in range(w)]for y in range(h)]
# print(matrix)
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print()
# for h in range(len(matrix)):
#     if h % 2 == 0:
#         h = matrix[h + 1]
#     else:
#         h = matrix[h - 1]
#     for w in h:
#         print(w, end="\t\t")
#     print()

# days = [d for d in range(1, 32)]
# print(days)
# weeks = [days[i:i+5] for i in range(0, len(days), 7)]
# print(weeks)
# for row in weeks:
#     for x in row:
#         print(x, end="\t\t")
#     print()


# import math  # (math.sqrt)
# import math as m  # (m.sqrt)
# from math import *  # (sqrt)

# print(math.sqrt(2))
# print(math.floor(3.8))# округление в меньшую сторону
# print(math.ceil(3.2)) # в большую сторону

# r = int(input("Введите радиус окружности: "))
# print("Длинна окружности: ", round(2 * pi * r, 2))

# lst = [1, 2, 3, 8.4]
# print(sum(lst))
# print(fsum(lst))
#
# print(degrees(3.14159)) # переводит из радиан в градусы
# print(radians(180)) #из градусов в радианы
#
# print(cos(radians(60)))

# a = int(input("Катет 1: "))
# b = int(input("Катет 2: "))
# print("Гипотенуза: ", sqrt((a ** 2) + (b ** 2)))

import time

# seconds = time.time()
# print(seconds)
# local_time = time.ctime(seconds)
# print(local_time)
# res = time.localtime(seconds)
# print(res)

# start = time.monotonic()
# time.sleep(5)
# finish = time.time()
# result = finish - start
# print(result)

# import locale
# locale.setlocale(locale.LC_ALL, "")
# print(time.strftime("Сегодня: %B %d %Y", time.localtime()))

print("hello")

