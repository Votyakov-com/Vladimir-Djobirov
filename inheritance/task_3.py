class BankAccount:
    def __init__(self, holder, balance, interest_rate):
        self.__holder = holder
        self.balance = balance
        self.interest_rate = interest_rate

    # Getting information about the holder of the account
    @property
    def holder(self):
        return self.__holder

    # Changing information about the holder of the account
    @holder.setter
    def holder(self, holder):
        self.__holder = holder

    def __str__(self):
        print(f'Holder: {self.__holder} \nBalance: ${self.balance:,} \nInterest_rate: {self.interest_rate}')


class BankOperation(BankAccount):
    List_of_history = []

    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance, interest_rate)

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.List_of_history.append(f'[Account cash deposit]: ${amount:,}')

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.List_of_history.append(f'[Account cash withdrawal]: ${amount:,}')

    def add_interest(self):
        rate = self.balance * self.interest_rate
        self.List_of_history.append(f'[Account accrued interest]: ${rate:,}')

    def history(self):
        for _ in self.List_of_history:
            print(_)
