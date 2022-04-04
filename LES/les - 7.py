import random as r

# city_list = ['Москва', 'Новосибирс', 'Воронеж', 'Сочи', 'Екатеренбург']
# print(r.choice(city_list))# choice возвращает рандомный один элеменит списка
# s = [55, 66, 77, 88, 99]
# print(r.choice(s))
# s3 = [20, 30, 40, 50, 60, 70, 80, 90]
# print(r.choices(s3, k=5))# k количесво случайных элементов
# r.shuffle(s3) # перемешивает список
# print(s3)
# print(r.uniform(10.5, 25.5)) # выводит вещественное число в диапазоне
# print(round(r.uniform(10.5, 25.5), 2))

# mas = [i for i in range(10)]
# print(mas)
#
# mas1 = [r.randint(0, 100) for i in range(10)] # всего чисел 10 а диапазон от 0 до 100
# print(mas1)

# lst = [5, 3, 2, 4, 1]
# print(len(lst)) # len длинна списка
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# sum = [5, 3, 2, 4, 1]
# print(min(sum))
# #print(sum(sum))
# print(sum(lst))
#
# a = [r.randint(0, 100) for i in range(10)]
# print(a)
# b = max(a)
# print("Max: ", b)
# a.remove(b)
# a.insert(0, b)
# print(a)

# n1 = 5
# n2 = 4
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for j in range(len(b)):
#     if b[j] not in c:
#         c.append(b[j])
# print("Элементы обоих списков без повторений: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
# c = [min(a), max(a), min(b), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m[1][2])
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     for col in row:
#         print(col, end="\t\t")
#     print()

# m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# for row in m:
#     for col in row:
#       print(col, end="\t\t")
#     print()
# print()
# for row in m:
#     for col in row:
#         print(col ** 2, end="\t\t")
#     print()
# print()

mas = [
    [2, 5, 8],
    [5, 8, 2],
    [8, 7, 1],
    [0, 7, 1],
    [9, 11, 6]
]
for row in mas:
    for col in row:
        print(col, end="\t")
    print()
print()
for i in range(len(mas)):
    if i % 2 == 0:
        mas[i].sort(reverse=True)
    else:
        mas[i].sort()
for row in mas:
    for col in row:
        print(col, end="\t")
    print()
