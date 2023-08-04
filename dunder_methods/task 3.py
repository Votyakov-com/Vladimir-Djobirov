from random import randint
class Item:

    def __init__(self, ID, price, rarity, color):
        self.ID = ID
        self.price = price
        self.rarity = rarity
        self.color = color

    def __lt__(self, other):
        if self.ID < other.ID:
            return True
        if self.ID > other.ID:
            return False
        if self.price < other.price:
            return True
        if self.price > other.price:
            return False
        if self.rarity < other.rarity:
            return False
        if self.rarity > other.rarity:
            return True
        if self.color > other.color:
            return True
        if self.color < other.color:
            return False

    def __eq__(self, other):
        return self.ID == other.ID and self.price == other.price and self.rarity == other.rarity and self.color == other.color

    def __le__(self):
        return self == other or self < other

    def __gt__(self, other):
        return self > other

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return self != other

    def __eq__(self, other):
        return self == other

    def __str__(self):
        return f"[ID]:{self.ID} [price]:{self.price} [RARITY]:{self.rarity} [color]:{self.color}"
    