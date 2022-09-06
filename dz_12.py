from math import pi


def square(figure_tupe, **kwargs):
    if figure_tupe == 'rhombus':
        return kwargs['d1'] * kwargs['d2'] / 2
    if figure_tupe == 'square':
        return kwargs['a'] * 2
    if figure_tupe == 'trapezoid':
        return 1 / 2 * (kwargs['a'] + kwargs['b']) * kwargs['h']
    if figure_tupe == 'circle':
        return kwargs['r'] ** 2 * pi
    if figure_tupe == 'unknown':
        print("invalid data")


print(square(figure_tupe='rhombus', d1=10, d2=8))
print(square(figure_tupe='square', a=5))
print(square(figure_tupe='trapezoid', a=12, b=3, h=6))
print(square(figure_tupe='circle', r=18))
print(square(figure_tupe='unknown', a=1, b=2, h=3))