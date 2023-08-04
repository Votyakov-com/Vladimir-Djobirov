import math


class Vector3:

    def __init__(self, x, y, z):
        self.coords = (x, y, z)

    def __add__(self, other):
        L1 = []
        for i in range(len(self.coords)):
            L1.append(self.coords[i] + other.coords[i])
        return Vector3(*L1).coords

    def __neg__(self):
        L2 = []
        for i in range(len(self.coords)):
            L2.append(self.coords[i] * (-1))
        return Vector3(*L2).coords

    def __sub__(self, other):
        L3 = []
        for i in range(len(self.coords)):
            L3.append(self.coords[i] - other.coords[i])
        return Vector3(*L3).coords

    def __len__(self):
        array_of_squary = list(map((lambda number: number ** 2), self.coords))
        return int(math.sqrt(sum(array_of_squary)))

    def __abs__(self):
        array_of_squary = list(map((lambda number: number ** 2), self.coords))
        return int(math.sqrt(sum(array_of_squary)))

    def __str__(self):
        return f"{'{'}{self.coords[0]}, {self.coords[1]}, {self.coords[2]}{'}'}"

    def __mul__(self, other):
        L4 = []
        for i in range(len(self.coords)):
            L4.append(self.coords[i] * other.coords[i])
        return Vector3(*L4).coords
    