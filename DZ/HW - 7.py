import random as r

a = [r.randint(0, 100) for i in range(20)]
print(a)
print("Summa: ", sum(a))


# Задание 2
m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
for row in m:
    for col in row:
        print(col, end="\t")
    print()
print()
i = 0
for col in row:
    for row in m:
        print(row[i], end="\t")
    i += 1
    print()



