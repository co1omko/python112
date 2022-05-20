import math


class Cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def __str__(self):
        return f"{self.r, self.h}"

    def get_volume(self):
        return round(math.pi * self.r ** 2 * self.h, 2)
