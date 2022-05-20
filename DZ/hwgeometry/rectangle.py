class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a, self.b}"

    def get_perimetr(self):
        return 2 * (self.a + self.b)

    def get_square(self):
        return self.a * self.b
