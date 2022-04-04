import random as r


# w, h = 6, 6
# matrix = [[r.randint(1, 100)for x in range(w)]for y in range(h)]
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print()
# d = [matrix[i][i] for i in range(len(matrix))]
# print("Минимальный элемент главной диагонали массива: ", min(d))
# print()
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print()
# # m = 0
# # for i in range(len(matrix)):
# #     for j in range(len(matrix[i])):
# #         if matrix[i][j] > m:
# #             m = matrix[i][j]
# # print("Максимальный элемент массива: ", m)
# m = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))]
# print("Максимальный элемент массива: ", max(m))



w, h = 6, 6
matrix = [[r.randint(0, 10)for x in range(w)]for y in range(h)]
for h in matrix:
    for w in h:
        print(w, end="\t\t")
    print()
print()
a = [r.randint(0, 10)for i in range(6)]
print(a)
for h in range(len(matrix)):
    if h % 2 != 0:
        matrix[h].clear()
        matrix[h].extend(a)
print()
for h in matrix:
    for w in h:
        print(w, end="\t\t")
    print()
print()


