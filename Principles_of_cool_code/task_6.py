class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, summ_of_money):
        self.balance += summ_of_money
        return f'[Операция]: На Ваш счёт было зачисленно: {summ_of_money:,}'

    def withdraw(self, summ_of_money):
        if self.balance < summ_of_money:
            return 'На Вашем счету недостаточно средств для снятия'
        else:
            self.balance -= summ_of_money
            return f'[Операция]: С Вашего счёта было снято: {summ_of_money:,}'

    def get_balance(self):
        return f'[Баланс]: {self.balance:,}'


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return f'Проценты по счету: {(self.balance * self.interest_rate * 0.01):,}'

    def get_interest_rate(self):
        percentages = self.balance * self.interest_rate * 0.01
        self.balance += percentages
        return f'[Операция]: На Ваш счет были зачислены проценты по вкладу на сумму: {percentages}'


class CheckingAccount(Account):
    def __init__(self, account_number, balance, fee_percentage):
        super().__init__(account_number, balance)
        self.fee_percentage = fee_percentage

    def get_fee_percentage(self):
        return f'Текущий процент коммисии: {self.balance * self.fee_percentage}'

    def deduct_fees(self):
        com_per = self.balance * self.fee_percentage
        self.balance -= com_per
        return f'С Вашего счета был вычтен коммиссионый процент в размере: {com_per}'


class Bank:
    list_of_accounts = []

    def get_account_number(self, account_number):
        for account in self.list_of_accounts:
            if account.account_number == account_number:
                return account
        raise KeyError('Такого счета не существует')

    def add_account(self, account):
        self.list_of_accounts.append(account)

    def get_account(self, index):
        print(self.list_of_accounts[index].account_number)

    def delete_account(self, account_number):
        array_of_numbers = []
        for i in range(len(self.list_of_accounts)):
            array_of_numbers.append(self.list_of_accounts[i].account_number)
        for index in range(len(array_of_numbers)):
            if account_number == array_of_numbers[index]:
                self.list_of_accounts[index] = 'Deleted account'
                print('Удаление... --> Успешно!')
        if (account_number in array_of_numbers) is False:
            raise KeyError('Такого счета не существует!')

    def transfer_funds(self, source_account_number, destination_account_number, amount):
        source_account = self.get_account_number(source_account_number)
        destination_account = self.get_account_number(destination_account_number)

        if source_account.balance >= amount:
            source_account.withdraw(amount)
            destination_account.deposit(amount)
            print('Перевод выполнен успешно!')
        else:
            print('Недостаточно средств на счете для перевода!')
