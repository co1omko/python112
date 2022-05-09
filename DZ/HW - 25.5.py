class DisTriangle:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'Значние должно быть целым числом')
        elif value < 0:
            raise ValueError(f'Значние должно быть положительным числом')
        instance.__dict__[self.name] = value


class Triangle:
    a = DisTriangle()
    b = DisTriangle()
    c = DisTriangle()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def prop(self):
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.b + self.a:
            return f'Треугольник со сторонами {self.a}, {self.b}, {self.c} существует'
        else:
            return f'Треугольник со сторонами {self.a}, {self.b}, {self.c} не существует'


t1 = Triangle(2, 5, 6)
print(t1.prop())
t2 = Triangle(5, 2, 8)
print(t2.prop())
t3 = Triangle(7, 3, 6)
print(t3.prop())