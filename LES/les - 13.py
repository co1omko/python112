# # frozenset -  вид множества которое не может быть измененно
# s = frozenset([1, 2, 3, 4, 5])
# print(s)

# dict - словарь

# ls = ["один", "два"]
# d = {"one": "один", "two": "два"}
# print(type(d))
# print(d["one"])

# d = {"one": "один", "two": "два"}
# print(type(d))
#
# d1 = dict(one="один", two="два")
# print(d1)

# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3)

# users = [
#     ['igor@gmail.com', 'Igor'],
#     ['irina@gmail.com', 'Irina'],
#     ['anna@gmail.com', 'Anna']
# ]
# print(users)
#
# d_users = dict(users)
# print(d_users)


# d4 = {i: i ** 2 for i in range(7)}
# print(d4)
# print(d4[5])


# d5 = {0: "text1", "one": 45, (1, 2, 3): 'кортеж', 42: [2, 3, 4, 5, 6], True: 1}
# key = "one1"
# if key in d5:
#     del d5[key]
# try:
#     del d5[key]
# except KeyError:
#     print("Элкмента с ключом", key, "нет в словаре")
# print(d5)
# del d5[(1, 2, 3)]
# print(d5)
# print("one" in d5)


# d6 = {'one': 1, 'two': 2, 'three': 3}
# for key in d6:
#     print(key, d6[key])


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# p = 1
# for key in d:
#     p *= d[key]
# print(p)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = {i: input("-> ")for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# capitals = dict()
# capitals['Россия'] = "Москва"
# capitals['Италия'] = "Рим"
# capitals['Испания'] = "Мадрид"
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print("Столица страны "+ country+": "+capitals[country])
#     else:
#         print("В базе нет страны с названием " + country)


# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i3-3450', 6, 6400]
# }
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб ", sep="")
# while True:
#     n = input("№: ")
#     if n != "0":
#         q = int(input("Количество: "))
#         goods[n][1] = q
#     else:
#         break
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб ", sep="")


# d = {"A": 1, "B": 2, "C": 3}
# x = iter(d)
# print(x)
# print(list(x))
# d.clear()
# print(d)

d = {"A": 1, "B": 2, "C": 3}
item = d.pop("B")
print(item)
# d = {"A": 1, "B": 2, "C": 3}
# d.update([("R", 7), ('Q', 9)])
# print(d)