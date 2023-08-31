import math


def circle(radius=5):
    return (f'Площадь окружности: {math.pi * radius ** 2}\n'
            f'Длина окружности: {2 * math.pi * radius}')


def triangle(side_one=7, side_two=2, side_three=8):
    hypotenuse = max(side_one, side_two, side_three)
    if hypotenuse > (side_one + side_two + side_three - hypotenuse):
        return 'Треугольник с данными сторонами не существует!'
    else:
        perimetr = side_one + side_two + side_three
        half_perimetr = perimetr / 2
        square_area = (half_perimetr * (half_perimetr - side_one) * (half_perimetr - side_two) * (
                half_perimetr - side_three))
        return (f'Периметр треугольника: {perimetr}\n'
                f'Площадь треугольника: {math.sqrt(square_area)}')


def square(side=15):
    return (f'Периметр квадрата: {side * 4}\n'
            f'Площадь квадрата: {side ** 2}')
