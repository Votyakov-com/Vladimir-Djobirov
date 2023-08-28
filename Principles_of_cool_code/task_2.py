class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price


class GiveDiscount(Discount):
    def __init__(self, customer, price):
        super().__init__(customer, price)

    def give_discount(self):
        if self.customer == 'FAV':
            return f'Ваша скидка: {self.price * 0.2}'
        if self.customer == 'VIP':
            return f'Ваша скидка: {self.price * 0.4}'
