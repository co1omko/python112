import math


class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f"{self.r}"

    def get_long(self):
        return round(2 * math.pi * self.r, 2)

    def get_square(self):
        return round(math.pi * self.r ** 2, 2)
