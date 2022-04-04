# def union(s):
#     if not s:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print("Выпрямленный список: ", union(names))

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\tWorld "))

# Поиск и сортировка


# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))


# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))


# бинарный поиск

# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(binary_search(lst, 3))
# print(binary_search(lst, 13))


import random as r



def bin(s, item):
    first = 0
    last = len(s) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if s[midpoint] == item:
            found = True
        else:
            if item < s[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    if found:
        print("Число", item, "в списке присутствует")
    else:
        print("Число", item, "в списке отсутствует")


lst = sorted([r.randint(1, 100) for i in range(10)])
print(lst)
a = int(input("Введите число: "))
bin(lst, a)

import time as t


# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#         #     print(a)
#         # print("-" * 40)
#
# a = [r.randint(1, 99) for i in range(10)]
# print(a)
# # start = t.monotonic()
# bubble(a)
# print(a)
# # res =  t.monotonic() - start
# # print(round(res, 3), "sec") # пузырьковая сортировка 6,813 сек


# сортировка слияние

# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#
#     return res
#
#
# array = [r.randint(1, 99) for i in range(10000)]
# # print(array)
# start = t.monotonic()
# array = merge_sort(array)
# # print(array)
# res = t.monotonic() - start
# print(round(res, 3), "sec") # слияние 0,047 сек

# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#         gap //= 2
#     #     print(gap, "Spisok: ", s)
#     # return s
#
#
# # a = [10, 44, 26, 14, 67, 21, 9, 87]
# a = [r.randint(1, 99) for i in range(10000)]
# #print(a)
# start = t.monotonic()
# shell_sort(a)
# # print(a)
# res = t.monotonic() - start
# print(round(res, 3), "sec") # сортировка шелла 0,031 сек


# a = [r.randint(1, 99) for i in range(10000)]
# start = t.monotonic()
# a.sort()
# res = t.monotonic() - start
# print(round(res, 3), "sec") # sort 0,031 сек