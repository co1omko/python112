import random as r


w, h = 6, 6
matrix = [[r.randint(0, 100)for x in range(w)]for y in range(h)]
for h in matrix:
    for w in h:
        print(w, end="\t\t")
    print()
print()
d = [matrix[i][i] for i in range(len(matrix))]
print("Миримальное число главной диагонали: ", min(d))


