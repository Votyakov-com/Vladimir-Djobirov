import math


def equation(a, b, c):
    discriminant = b ** 2 - (4 * a * c)
    if discriminant > 0:
        x1 = ((-1) * b + math.sqrt(discriminant)) / 2 * a
        x2 = ((-1) * b - math.sqrt(discriminant)) / 2 * a
        return f'x1 = {x1}, x2 = {x2}'
    if discriminant == 0:
        x = ((-1) * b) / 2 * a
        return f'x = {x}'
    if discriminant < 0:
        return 'В данном уравнении нет корней! (Ø)'
