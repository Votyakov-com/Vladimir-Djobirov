import math


class Vector2:

    def __init__(self, x, y):
        self.coords = (x, y)

    def __len__(self):
        array_of_squares = list(map((lambda number: number ** 2), self.coords))
        return int(math.sqrt(sum(array_of_squares)))

    def __add__(self, other):
        L1 = []
        for i in range(len(self.coords)):
            L1.append(self.coords[i] + other.coords[i])
        return Vector2(*L1)

    def __neg__(self):
        L2 = []
        for i in range(len(self.coords)):
            L2.append(self.coords[i] * (-1))
        return Vector2(*L2)

    def __sub__(self, other):
        L3 = []
        for i in range(len(self.coords)):
            L3.append(self.coords[i] - other.coords[i])
        return Vector2(*L3)

    def __abs__(self):
        array_of_squares = list(map((lambda number: number ** 2), self.coords))
        return int(math.sqrt(sum(array_of_squares)))

    def __eq__(self, other):
        array_of_squares__self_coords = list(map((lambda number: number ** 2), self.coords))
        array_of_squares_other_coords = list(map((lambda number: number ** 2), other.coords))
        return int(math.sqrt(sum(array_of_squares__self_coords))) == int(math.sqrt(sum(array_of_squares__other_coords)))

    def __str__(self):
        return f'{"{"}{self.coords[0]}, {self.coords[1]}{"}"}'

    def __mul__(self, other):
        L4 = []
        for i in range(len(self.coords)):
            L4.append(self.coords[i] * other.coords[i])
        return Vector2(*L4)