# print('I\'m learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file\\'[:-1])
# print(r'C:\file' + '\\')
# print('C:\\file\\')

# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")


# import math as m
#
# print(f"Значение числа pi: {m.pi:.2f}")
# print(f"13 / 3 = {round(13 / 3, 2) }")

# a = [1, 2, 3, 4, 5, 6]
# print(f"Третий элемент списка {a[3] * 2}")

# name = "друг"
# prof = "программист"
# lang = "Python"
# message = (
#     f"Привет {name}."
#     f"Ты {prof}."
#     f"На языке {lang}."
# )
# print(message)

# a = 74
# print(f"{{{a}}}")

# d = "my_doc"
# f = "data.txt"
# print(fr"home\{d}\{f}")
# print("home\\" + d + "\\" + f)


#  '''
# <div>
#     <a href=""#>content</a>
# </div>
# '''
# s =
# print(s)

# def square(n):
#     """Принимает число n, возвращает квадрат сисла n"""
#     return n ** 2
#
# print((square(5)))
# print(square.__doc__)

# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заджанной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# a = "hi"
# b = 'hi'
# c = """hi"""
# d = '''hi'''
# print(f"{a} {b} {c} {d}")

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII коды", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [x for x in [ord(x)for x in (input("-> ")[:3])] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(40))

# a = 122
# b = 97
# for x in range(b, a, +1):
#     print(chr(x), end=" ")

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST) # случайная длинна пароля
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print(random_password())

#
s = "hello, WORLD! I am learning Python"
# print(s.capitalize()) # Hello, world! i am learning python
# print(s.lower()) # hello, world! i am learning python
# print(s.upper()) # HELLO, WORLD! I AM LEARNING PYTHON
# print(s.swapcase()) # HELLO, world! i AM LEARNING pYTHON
# print(s.title()) # Hello, World! I Am Learning Python
#
#
# print(s.count("h", 0, -4)) # количество заданных символов
# print(s.find("Python")) # возвращает первый индекс задданых символов
print(s.index("Python")) # возвращает первый индекс задданых символов

# s = 'один два'
# s2 = s[s.find(' ') + 1:] + ' ' + s[:s.find(' ')]
# print(s2)

# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if '0123456789'.find(i) != -1:
#         digits.append(int(i))
# print(digits)
