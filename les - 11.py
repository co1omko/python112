# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = (input("Введите пароль: "))
# if check_password(p):
#     print("Это надежный пароль: ")
# else:
#     print("Это не надежный пароль: ")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def set_param(x=20, y="-"):
#     print(x*y)
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()

# def check_password(username, password, min_len=8, check_user=True):
#     if len(password) < min_len:
#         print("Пароль слишком короткий")
#         return False
#     elif check_user and username in password:
#         print("Пароль содержит имя пользователя!")
#         return False
#     else:
#         print("Пароль для пользователя", username, "прошел все проверки)")
#
#
# check_password("igor", "12345")
# check_password("igor", "12345igor")
# check_password("igor", "12345name")

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2 == 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четныйх цыфр: ")
# print(digit_sum(9814023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетныйх цыфр: ")
# print(digit_sum(9814023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name: ", name, "\nAge: ", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
#
#
# print(func(1))
# print(func(2))
# print(func(3))


# lt1= [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
#
# print(lt1 == lt2)
# print(lt1 is lt2)

# a = (1, 2, 3, 4, 5)
# print(a)
# print(type(a))
# b = 1, 2, 3
# print(tuple(b))
# print(type(b))

# t = ()
# print(type(t))
#
# a = tuple((1, 2, 3, 4, 5))
# print(a)
#
# print(a[1:3])

# s1 = tuple(int(input("-> ")) for i in range(1, 6))
# print(s1)

import random

s = tuple(2 ** i for i in range(1, 13))
print(s)
