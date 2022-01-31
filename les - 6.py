# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s[1:3])
# s[1:3] = [20]
# print(s)
# s[4] = 30
# print(s)

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s.append(99)
# print(s)
# s.extend([11, 77, 66])
# print(s)


# a = []
# for i in range(1, 11):
#     a.extend([i ** 2])
# print(a)

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s.insert(2, 100)
# print(s)



# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# lst = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         lst.extend([x])
#     else:
#         print(x, "не делится на 3 без остатка.")
# print(lst)


# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s.remove(2)
# print(s)

# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# print("Введите индекс: ")
# k = int(input("k = "))
# c = []
# a.pop(k)
# print(a)

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# # num = s.count(2)
# # print(num)
# # print(s)
# for i in s:
#     if s.count(i) == 1:
#         print(i, end=" ")

s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
print(s)
ind = s.index(3)
print(ind)