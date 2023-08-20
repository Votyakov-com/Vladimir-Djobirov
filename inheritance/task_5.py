class Investments:
    def __init__(self, ticker, price, currency, industry, counter):
        self.ticker = ticker
        self.price = price
        self.currency = currency
        self.industry = industry
        self.counter = counter

    def display(self):
        array_of_name_attr = ['Ticker', 'Price', 'Currency', 'Industry', 'Counter']
        array_of_attr = [self.ticker, self.price, self.currency, self.industry, self.counter]
        for _ in range(max(len(array_of_attr), len(array_of_name_attr))):
            print(f'[{array_of_name_attr[_]}]: {array_of_attr[_]}')


class Shares(Investments):
    def __init__(self, ticker, price, currency, industry, counter, dividend, echelon, profit):
        super().__init__(ticker, price, currency, industry, counter)
        self.dividend = dividend
        self.echelon = echelon
        self.profit = profit

    def buying(self):
        if self.profit > 5:
            result = self.price * self.counter
            print(f'[A purchase has been made for the amount of]: '
                  f'{result:,} {self.currency} Congratulations!')
        else:
            print(f'Your profit is too small!')


class Bonds(Investments):
    def __init__(self, ticker, price, currency, industry, counter, coupon, echelon, nominal):
        super().__init__(ticker, price, currency, industry, counter)
        self.coupon = coupon
        self.echelon = echelon
        self.nominal = nominal

    def buying(self):
        if self.price <= self.nominal:
            result = self.price * self.counter
            print(f'[A purchase has been made for the amount of]: '
                  f'{result:,} {self.currency} Congratulations!')
