class HeavenlyBody:
    """Parent class HeavenlyBody"""

    def __init__(self, name, age, temperature, radius):
        self.name = name
        self.age = age
        self.temperature = temperature
        self.radius = radius

    def display(self):
        print(f'[Name: {self.name}] '
              f'[Age: {self.age} million years] [Temperature: {self.temperature}] [Radius: {self.radius}]')


class Planet(HeavenlyBody):
    """Child class Planet"""

    def __init__(self, name, age, temperature, radius, speed_orbital):
        super().__init__(name, age, temperature, radius)
        self.speed_orbital = speed_orbital

    def display(self):
        print(f'[Name: {self.name}] '
              f'[Age: {self.age} million years] [Temperature: {self.temperature}] '
              f'[Radius: {self.radius}] [Orbital_speed: {self.speed_orbital}]')


class Star(HeavenlyBody):
    """Child class Start"""

    def __init__(self, name, age, temperature, radius, constellation):
        super().__init__(name, age, temperature, radius)
        self.constellation = constellation

    def display(self):
        print(f'[Name: {self.name}] '
              f'[Age: {self.age} million years] [Temperature: {self.temperature}] '
              f'[Radius: {self.radius}]'
              f'[Constellation : {self.constellation}]')
