def dec(func):
    def wrap(*args):
        print("Сумма чисел", args, "=", func(*args))
        print("Среднее арифметическое чисел", args, "=", func(*args) / len(args))

    return wrap


@dec
def summa(*args):
    return sum(args)


summa(2, 3, 3, 4)

# Здание 2
# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == old and i % 2 == 0:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык програмирования.'
# str2 = change_char_to_str(str1, 'N', 'P')
# print("str1 = ", str1)
# print("str2 = ", str2)

# Здание 3
# s = "012345678"
# s = s[:4] + s[5:]
# print('s2 =', s)

# Здание 4
# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = '012345363738494'
# str2 = change_char_to_str(str1, '3', '')
# print("str1 = ", str1)
# print("str2 = ", str2)
