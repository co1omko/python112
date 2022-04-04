#Задание 1
a = [int(input("-> ")) for i in range(int(input("n = ")))]
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i], end=" ")

#Задание 2
a = [int(input("-> ")) for i in range(int(input("n = ")))]
b = 1
for i in range(len(a)):
    if a[b] > a[b - 1]:
        print(a[b], end=" ")
    b += 1

#Задание 3
a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
print(a)
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=" ")
