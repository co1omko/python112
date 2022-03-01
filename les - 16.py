# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# локальная переменная

# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + (rect_square(b, c)))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# глобальная переменная

# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + (rect_square(b, c)))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(s)
# print(rect_paral_square(5, 8, 2))
# print(s)
# print(rect_paral_square(1, 6, 8))
# print(s)


# нелокальная переменная

# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(b, c)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# print(outer(5)(10))
# # add5 = outer(5)
# # print(add5(10))
# # print(add5(4))
# # add6 = outer(6)
# # print(add6(10))

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         b = b + " 2"
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     a = 0
#
#     def func1():
#         nonlocal a
#         a += 1
#         print(city, a)
#     return func1
#
#
# res = func('Москва')
# res()
# res()
#
# res2 = func('Сочи')
# res2()
# res2()
#
# res()


# students = {
#     "Alice": 98,
#     "Bob": 67,
#     "David": 85,
#     "Chris": 75,
#     "Ella": 54,
#     "Fiona": 35,
#     "Grace": 69
# }
#
# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for (k, v) in exam.items() if lower <= v < upper}
#
#     return inner
#
# a = outer(80, 100)
# b = outer(70, 80)
# c = outer(50, 70)
# d = outer(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))


# def func_object(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#
#     return replace
#
#
# obj1 = func_object(5, 2)
# print(obj1.add())
#
# obj2 = func_object(5, 2)
# print(obj2.sub())
#
# obj3 = func_object(5, 2)
# print(obj3.mul())


# def func(x1, y1):
#     return x1, y1
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))


# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ())

# func = lambda *args: args
#
# print(func(1, 2, 3, 4))


# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
# for t in c:
#     print(t('abc'))


# print((lambda x: (lambda y: (lambda z: x + y + z)))(2)(4)(6))


# d = {'a': 10, 'b': 15, 'c': 4}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1])
# print(list_d)

a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
b = a[0](12, 6)
print(b)
print(type(lambda x, y: x - y))
