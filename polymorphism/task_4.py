from abc import ABC, abstractmethod


class GeometricFigures(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass


class Triangle(GeometricFigures):
    def __init__(self, side_one, side_two, side_three):
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three

    def get_perimeter(self):
        return (
            f'Периметр:{self.side_one + self.side_two + self.side_three}')

    def __str__(self):
        return f'Треугольник со сторонами {self.side_one}, {self.side_two}, {self.side_three}.'


class Square(GeometricFigures):
    def __init__(self, side):
        self.side = side

    def get_perimeter(self):
        return f'Периметр: {self.side * 4}'

    def __str__(self):
        return f'Квадрат со стороной {self.side}.'


class Rectangle(GeometricFigures):
    def __init__(self, side_one, side_two):
        self.side_one = side_one
        self.side_two = side_two

    def get_perimeter(self):
        return (
            f'Периметр: {(self.side_one + self.side_two) * 2}')

    def __str__(self):
        return f'Прямоугольник со сторонами {self.side_one}, {self.side_two}.'
