class Pastry:
    def __init__(self, name, price, manufacture_date, term):
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date
        self.term = term

    def display(self):
        array_of_attributes = [self.name, self.price, self.manufacture_date, self.term]
        array_of_names = ['name', 'price', 'manufacture_date', 'term']
        for attribute in range(len(array_of_attributes)):
            print(f'{array_of_names[attribute]}: {array_of_attributes[attribute]}')

    def valid_until(self):
        if self.term == self.manufacture_date:
            print('Today is the last day!')
        elif int(self.term[6:]) < int(self.manufacture_date[6:]) or (
                int(self.term[6:]) == int(self.manufacture_date[6:])
                and int(self.term[3:5]) < int(self.manufacture_date[3:5])):
            print('The expiration date has already expired!')
        else:
            days = abs(int(self.term[0:2]) - int(self.manufacture_date[0:2]))
            months = abs(int(self.term[3:5]) - int(self.manufacture_date[3:5]))
            years = abs(int(self.term[6:]) - int(self.manufacture_date[6:]))
            print(f'Remained: {days + months * 30 + years * 365} days')


class Cake(Pastry):
    def __init__(self, name, price, manufacture_date, term, filling):
        super().__init__(name, price, manufacture_date, term)
        self.filling = filling

    def order(self):
        array_of_attributes = [self.name, self.price, self.manufacture_date, self.term, self.filling]
        array_of_names = ['name', 'price', 'manufacture_date', 'term', 'filling']
        for attribute in range(len(array_of_attributes)):
            print(f'{array_of_names[attribute]}: {array_of_attributes[attribute]}')
        self.valid_until()


class BentoCake(Pastry):
    def __init__(self, name, price, manufacture_date, term, celebration):
        super().__init__(name, price, manufacture_date, term)
        self.celebration = celebration

    def order(self):
        array_of_attributes = [self.name, self.price, self.manufacture_date, self.term, self.celebration]
        array_of_names = ['name', 'price', 'manufacture_date', 'term', 'celebration']
        for attribute in range(len(array_of_attributes)):
            print(f'{array_of_names[attribute]}: {array_of_attributes[attribute]}')
        self.valid_until()
