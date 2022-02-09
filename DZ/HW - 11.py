import random as r

# def slicer(tup, elem):
#     if elem in tup:
#         if tup.count(elem) > 1:
#             fir = tup.index(elem)
#             sec = tup.index(elem, fir + 1) + 1
#             return tup[fir:sec]
#         else:
#             return tup[tup.index(elem):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


tup1 = tuple(r.randint(0, 6) for i in range(10))
tup2 = tuple(r.randint(-6, 0) for j in range(10))
tup3 = tup1 + tup2
print(tup3)
print("0 =", tup3.count(0))
