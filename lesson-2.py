#a = int(input())
#b = int(input())
#c = int(input())
#if a == b == c:
#    print("Треугольник равносторонний")
#elif a == b or b == c or a == c:
#    print("Треугольник рввнобедренный")
#else:
#    print("Треугольник разносторонний")

#month = int(input("Введите номер месяца"))
#    if month == 1 or month == 2 or month == 12:
#    if month == 3 or month == 4 or month == 5:
#        print("Весна")
#    if month == 6 or month == 7 or month == 8:
#        print("Лето")
#    if month == 9 or month == 10 or month == 11:
#        print("Осень")
#else:
#    print("Ошибка данных")

#lesson 3
#a = int(input("Введите число от 1 до 99: "))
#kop = a
#if 11 <= kop <= 14:
#    print (a, "копеек")
#else:
#    kop = a % 10
#    if kop <= 1:
#        print(a, "копейка")
#    elif 2 <= kop <= 4:
#        print(a, "копейки")
#    else:
#        print(a, "копеек")


#a, b = 20, 20
#print("a == b" if a == b else ("a > b" if a > b else "b > a"))

#a, b = 2, 5
#print("на ноль делить нельзя" if a == 0 else b / a)


#n = input("Введите первое число: ")
#m = input("Введите второе число: ")
#try:
#    n = int(n)
#    m = int(m)
#except ValueError:
#    n = str(n)
#    m = str(m)
#finally:
#    print(n + m)

#i = 2
#while i < 22:
#    print("i =", i)
#    i += 2

#i = 1
#while i < 20:
#    i += 1
#    if i % 2 == 0:
#        print("i = ", i)

#a = int(input("Ввкдите количесиво символов: "))
#while a > 0:
#    print("*", end="")
#    a -= 1

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
s = 0
while a <= b:
    if a % 2 != 0:
        s += a
    a += 1
print(s)