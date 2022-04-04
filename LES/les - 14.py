# a = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")

# d = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
# }
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ": ", d[x][y], sep="")
# n = input("Имя: ")
# r = input("Регион: ")
# print(d[n][r])
# d[n][r] = int(input("Новое значение: "))
# print(d[n])

# a = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# b = {value: key for key, value in a.items()}
# print(b)

# a = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# b = {value: key for key, value in a.items() if value <= 2}
# print(b)


# v = int(input("-> "))
# s = [10, 20, 30, 40]
# a = {i: v for i in s}
# print(a)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = {}
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)


# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)


# a = ["Dec", "Jan", "Feb"]
# b = [12, 1, 2]
# f = {k: v for k, v in zip(b, a)}
# print(f)

# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# b = {'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55}
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs) #распаковк последовательносьти
# print(a)
# print(b)

# month = ["January", "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# production_cost = [46800.00, 45900.00, 43200.00]
# for sales, cost, m in zip(total_sales, production_cost, month):
#     res = sales - cost
#     print("Общая прибыль в", m, "=", res)


# one = {'apple': 0.04, 'orange': 0.35}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**two, **one}) #совмещение двух словарей
# for k, v in {**two, **one}.items():
#     print(k, '->', v)


# colors = ["red", "green", "blue"]
# # ind = 1
# # for color in colors:
# #     print(str(ind) + ') ' + color)
# #     ind += 1
#
# for i, color in enumerate(colors, 100):
#     print(str(i) + ') ' + color)

