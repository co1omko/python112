class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def cords(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __floordiv__(self, other):
        return Point3D(self.x // other.x, self.y // other.y, self.z // other.z)

    def __ge__(self, other):
        return self.x >= other.x, self.y >= other.y, self.z >= other.z

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('Ключ должен быть строкой')
        if item == 'x':
            return self.x
        elif item == 'y':
            return self.y
        elif item == 'z':
            return self.z

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Ключ должен быть строкой')
        if not isinstance(value, int):
            raise ValueError('Значение должно быть целым числом')
        x = self.x
        y = self.y
        z = self.z
        if key == 'x':
            self.x = value
        elif key == 'y':
            self.y = value
        elif key == 'z':
            self.z = value


p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)
print('Координаты 1-й точки:', p1.cords())
print('Координаты 2-й точки:', p2.cords())
p3 = p1 + p2
print('Сложение координат:', p3.cords())
p3 = p1 - p2
print('Вычитание координат:', p3.cords())
p3 = p1 * p2
print('Умнодение координат:', p3.cords())
p3 = p1 // p2
print('Деление координат:', p3.cords())
print('Равенсво уоординат:', p1 >= p2)
print('x =', p1['x'], 'x1 =', p2['x'])
print('y =', p1['y'], 'y1 =', p2['y'])
print('z =', p1['z'], 'z1 =', p2['z'])
p1['x'] = 20
print('Запись значения в координату x:', p1['x'])
