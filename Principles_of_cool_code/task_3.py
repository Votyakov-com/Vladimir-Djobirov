from abc import abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


def calculate_total_area(l1):
    summ_square = 0
    for element in l1:
        summ_square += element.area()
    return summ_square
