# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))

from random import randint

#
# x = [randint(0, 9) for i in range(10)]
# print(x)
#
#
# def func(s):
#     ls = []
#     for i in s:
#         if i not in ls:
#             ls.append(i)
#     print(ls)
#     return tuple(reversed(ls))
#
#
# print(func(x))
# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t
# print(x, y, z) #распоковка кортежа
#
#
# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# n, a, i = user
# print(n, a, i)


# t = (1, 2, 3)
# del t[0]
# print(t)


# lst = [1, 2, 3, 4, 5]
# print(type(lst))
# print(lst)
# t = tuple(lst)
# print(type(t))
# print(t)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))), ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, "население = ", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, "население = ", city_population)


# Множества (set)
# s = {1, 2, 1, 2, 3, 2, 3}
# print(s)
# print(len(s))
# c = ["hello", "hi", "hi"]
# a = set(c)
# b = {"hello", "hi", "hi"}
# print(b)


# s = {x * x for x in range(10) if x % 2 == 0}
# print(s)
# print(list(s))
# print(tuple(s))


# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6]
# print(list(set(numbers)))


# def to_set(element):
#     for i in element:
#


# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)

a = {0, 1, 2, 3}
a.add(4)
print(a)
