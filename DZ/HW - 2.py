# 1 задание
a = 1
b = 2
print("a:", a + 1)
print("b:", b - 1)

# 2 задание
name = input("What ois your name? ")
old = input("How old are you? ")
live = input("Where are ypu live? ")
print("This is", name)
print("It is", old)
print("He lives in", live)

# 3 задание
examp = int(input("Решите пример 4 * 100 - 56 = "))
print("Ваш ответ", examp)

# 4 задание
num = int(input("Введите пятизначное число "))
a = num % 10
num = num // 10
b = num % 10
num = num //10
c = num % 10
num = num // 10
d = num % 10
num = num // 10
e = num % 10
num = num // 10
print("Произведение цифр числа: ", a * b * c * d * e)
print("Среднее арифметическое: ", (a + b + c + d + e) / 5)


