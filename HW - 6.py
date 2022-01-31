# # Задание 1
# a = [int(input("Введите элементы списка: "))for i in range(int(input("Введите длину списка: ")))]
# print("Список: ", a, end=" ")
# b = []
# m = a
# for i in range(len(a)):
#     if a[i] >= 0:
#         b.append(a[i])
# print("\nНовый список, состоящий из положительных чисел: ", b, end=" ")
# a.sort()
# print("\nНаибольшее число списка: ", a[-1])
#
# # Задание 2
# print("Введите элементы списка:")
# a = [int(input("-> "))for i in range(int(input("n: ")))]
# k = c = 0
# print("Введите индекс:")
# k = int(input("k = "))
# print("Введите значение")
# c = int(input("c = "))
# a.insert(k, c)
# print(a)
#
# # Задание 3
# import random
# a = [random.randint(0, 100)for i in range(10)]
# print(a)
# a.sort(reverse=True)
# print(a)

# Задание 4
print("Введите элементы списка:")
a = [int(input("-> "))for i in range(int(input("n: ")))]
print("Введите число: ")
ch = int(input("ch = "))
for i in range(len(a)):
    if ch == a[i]:
        print("Число присутствует в элементах списка")


