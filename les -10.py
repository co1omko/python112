# Функции
# def hello(name, word): # аргументы
#     print("Hello,", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi") # параметры
# hello("Ivan", "hello")

# def get_sum(a, b):
# #     print(a + b)
# #
# #
# # x = 2
# # y = 5
# # get_sum(x, y)
# # get_sum("abc", "def")
# # get_sum(2.5, 4.3)

# def symbol(ch, sym1, sym2):
#     s = ""
#     for i in range(ch):
#         if i % 2 == 0:
#             s += sym1
#         else:
#             s += sym2
#     print(s)
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     print("Строка")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     elif two > one:
#         return two
#     else:
#         return
#
#
# m = maximum(9, 9)
# print(m)


# def add(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# m = add(a, b)
# print("Результат: ", m)

# def cube (a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# ряд фибоначи - каждое следующее число равно сумме двух предыдущих
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b
#         c = a + b
#         a = b
#         b = c
#
#
# fib(25)

def change(s):
    start = s.pop()
    end = s.pop(0)
    s.append(end)
    s.insert(0, start)
    return s
    # s[0], s[-1] = s[-1], s[0]
    # return s
    # # a = lst[0]
    # # b = lst[-1]
    # # for i in range(len(lst)):
    # #     if i == 0:
    # #         lst[i] = b
    # #     if i == len(lst) - 1:
    # #         lst[i] = a
    # #     print(lst[i], end=" ")
    #

print(change([1, 2, 3]))
print(change([9, 12, 33, 54, 105]))
print(change(["с", "л", "о", "н"]))
