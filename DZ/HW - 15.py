from math import pi


def square(figure_type, **kwargs):
    if figure_type == 'rhombus':
        return kwargs['d1'] * kwargs['d2'] / 2
    elif figure_type == 'square':
        return kwargs['a'] ** 2
    elif figure_type == 'trapezoid':
        return (kwargs['a'] + kwargs['b']) * kwargs['h'] / 2
    elif figure_type == 'circle':
        return pi * kwargs['r'] ** 2


print(square(figure_type="rhombus", d1=10, d2=8))
print(square(figure_type="square", a=5))
print(square(figure_type="trapezoid", a=12, b=3, h=6))
print(square(figure_type="circle", r=18))
