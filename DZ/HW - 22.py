# def num(s):
#     n = 0
#     for i in s:
#         if i < 0:
#             n += 1
#     print("n =", n)
#
#
# a = [-2, 3, 8, -11, -4, 6]
# print(a)
# num(a)


def sort(s):
    gap = len(s)

    while gap > 0:
        for val in range(gap, len(s)):
            cur_val = s[val]
            pos = val

            while pos >= gap and s[pos - gap] > cur_val:
                s[pos] = s[pos - gap]
                pos -= gap
                s[pos] = cur_val
        gap //= 2


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
        print("Значение", item, "найдено")
    else:
        print("Значение", item, "не найдено")


lst1 = [5, 9, 6, 7]
lst2 = [3, 11, 8]
lst3 = [2, 4]
lst4 = [10, 1, 12]
lst5 = lst1 + lst2 + lst3 + lst4
print(lst1, lst2, lst3, lst4)
sort(lst5)

print('1 - сортировка по убыванияю\n''2 - сортировка по возрастанию')
a = (int(input('-> ')))
if a == 1:
    print(lst5[::-1])
elif a == 2:
    print(lst5)
else:
    print("ERROR")

b = int(input("Введите значение для поиска: "))
bin(lst5, b)
