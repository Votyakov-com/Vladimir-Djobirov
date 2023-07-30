class CoffeMachine:
    def __init__(self, water_level, coffee_level, milk_level, sugar_level=0, cups=0):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.cups = cups

    def add_water(self, amount):
        return self.water_level + amount

    def add_coffee(self, amount):
        return self.coffee_level + amount

    def add_milk(self, amount):
        return self.milk_level + amount

    def add_sugar(self, amount):
        return self.sugar_level + amount

    def add_cups(self, number):
        return self.sugar_level + number

    def check_resources(self):
        if self.water_level >= 1 and self.coffee_level >= 1 and self.milk_level >= 1 and self.sugar_level >= 1 and self.cups >= 1:
            return True
        else:
            False

    def make_coffee(self):
        if self.check_resources():
            self.water_level -= 1
            self.coffee_level -= 1
            self.milk_level -= 1
            self.sugar_level -= 1
            self.cups -= 1
            return 'Кофе готов!'
        else:
            return 'Недостаточно ингредиентов!'