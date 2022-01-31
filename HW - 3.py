#Задание 1
i = int(input("Количество символов: "))
n = input("Тип символов: ")
l = int(input("0 - горизонтальная; ""1 - вертикальная; ""Ориентация линии: "))
print("Ориентация линии: ", l)
while i > 0:
    if l == 1:
        print(n)
        i -= 1
    print(n, end=" ")
    i -= 1

#Задание 2

kol = int(input("Введите количество чисел последовательно: "))
i = 1
ch = float(input("Введите число: "))
min_ch = ch
max_ch = ch
sum_ch = ch
while i < kol:
    ch = float(input("Введите число: "))
    sum_ch += ch
    if ch < min_ch:
        min_ch = ch
    if ch > max_ch:
        max_ch = ch
    i += 1
averange = sum_ch / kol
print("Максимальное число: ", max_ch)
print("Минимальное число: ", min_ch)
print("Среднее арифметическое ", averange)

#Задание 3
a = int(input("Введите число: "))
b = 0
c = 0
ans = a
while a > 0:
    b = a % 10
    c = c * 10
    a = a // 10
if c == ans:
    print("Число " + str(ans) +  " - палиндром")
else:
    print("Число " + str(ans) + " - не палиндром")
