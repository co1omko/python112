import re

# s = "Wprd2016, PS6, AI5"
# reg = r'([a-z]+)(\d*)'
# reg1 = r'([a-z]+\d*)'
# print(re.findall(reg, s, re.I))
# print(re.findall(reg1, s, re.I))

# 192.168.255.255  192.168.0.1

# s = '127.0.0.1'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s))

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# s = "28-09-2021"
# p = r'([0][1-9]|[0-2][0-9]|[3][0-1])-([0][1-9]|[1][0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(p, s))

# s = "Я ищу совпадения в 2021 году. И я их обязательно найду."
# reg = r'(\d+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print("Найдена строка:", m[0])
# print("Найдены цифры:", m[1])
# print("Найдены буквы:", m[2])
# print(re.findall(reg, s))

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>"
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# (?P<name>...) (?P=name)
# s = "<p>Изображение <img src=\"bg.jpg\"> - фон страницы</p>"
# # reg = r'<img\s+[^>]*src=[\'"].+[\'"]>'
# reg = r'<img\s+[^>]*src=(?P<q>[\'"])(.+)(?P=q)>'
# print(re.findall(reg, s))

# s = "Самолет прилетает 10/23/2021. Будем рады вас видеть после 10/24/2021"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "google.com and google.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком Вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
# print(sum_list([1, 3, 5, 7, 9]))


def to_str(n, base):
    convert = "0123456789ABCDEF"
    if n < base:
        return convert[n]
    else:
        return to_str(n // base, base) + convert[n % base]



print(to_str(255, 16))


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
#
#
# def count_items(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
# print(count_items(names))
