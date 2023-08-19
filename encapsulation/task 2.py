from random import choice
from random import randint


class Emerald:
    def __init__(self):
        self.__status = 0
        self.__price = 0

    # Getting information about the status of the emerald
    @property
    def emerald_status(self):
        return f'[Current status of the emerald]: {self.__status}'

    # Changing information about the status of the emerald
    @emerald_status.setter
    def emerald_status(self, status):
        if status >= self.__status and type(status) == int:
            self.__status = status
        else:
            print('The status of the emerald you entered is less than the original one or not int!')

    def account(self):
        if self.__status == 0:
            self.__status = 1
            self.__price = randint(100, 1000)
        else:
            raise IndexError("The status should not decrease!")

    def store(self):
        if self.__status == 1:
            self.__status = 2
            self.__price = randint(100, 1000)
        else:
            raise IndexError("The status should not decrease!")

    # Getting information about the price of the emerald
    @property
    def emerald_price(self):
        return f'[Current price]: {self.__price:,}$'

    # Changing information about the price of the emerald
    @emerald_price.setter
    def emerald_price(self, price):
        if type(price) == int:
            self.__price = price
        else:
            raise TypeError("The price must be in int format")


class Shell:
    def __init__(self):
        self.__status = 0
        self.__price = 0

    # Getting information about the status of the shell
    @property
    def shell_status(self):
        return f'[Current shell status]: {self.__status}'

    # Changing information about the status of the shell
    @shell_status.setter
    def shell_status(self, status):
        if type(status) == int and status >= self.__status:
            self.__status = status
        else:
            print('The status of the emerald you entered is less than the original one or not int!')

    def account(self):
        if self.__status == 0:
            self.__status = 1
            self.__price = randint(100, 1000)
        else:
            raise IndexError("The status should not decrease!")

    def process(self):
        if self.__status == 1:
            self.__status = 2
            self.__price = randint(100, 1000)
        else:
            raise IndexError("The status should not decrease!")

    # Creating a coin
    def smelt(self):
        if self.__status == 2:
            self.__status = 3
            if self.__status == 3:
                serial_number = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + '-' + str(
                    randint(0, 9)) + str(
                    randint(0, 9)) + str(randint(0, 9))
                year = randint(1970, 2023)
                value = choice(['dollar', 'ruble', 'shilling', 'penny'])
                item = Coin(serial_number, year, value)
                day = randint(1, 31)
                month = randint(1, 12)
                year = randint(1900, 2022)
                date = f"{day:02d}.{month:02d}.{year}"

                name_of_archive.add(Entry(item, date, info="Coin created", secret=False))

    # Getting information about the price of the shell
    @property
    def shell_price(self):
        return f'[Current shell price]: {self.__price:,}$'

    # Changing information about the price of the shell
    @shell_price.setter
    def shell_price(self, price):
        if type(price) == int:
            self.__price = price
        else:
            raise TypeError("The price must be in int format")


class Coin:
    def __init__(self, serial_number, year, value):
        self.__serial_number = serial_number
        self.__year = year
        self.__value = value

    # Getting information about the serial number of the coin
    @property
    def serial_number(self):
        return f'[Current serial number]: {self.__serial_number}'

    # Getting information about the year of the coin
    @property
    def year(self):
        return f'[Year of release]: {self.__year}'

    # Getting information about the value of the coin
    @property
    def value(self):
        return f'[Current coin value]: {self.__value}'


class Archive:
    def __init__(self):
        self.__storage = []

    # Adding an entry to the archive
    def add(self, info):
        self.__storage.append(info)

    # Getting information from the archive
    def get_info(self, index):
        try:
            if self.__storage[index] is not None and type(index) == int and self.__storage[index].secret is False:
                return f'[OBJECT REFERENCE]:[{self.__storage[index].item}] ' \
                       f'[DATE]:[{self.__storage[index].date}] [INFO]:[{self.__storage[index].info}]'
            elif self.__storage[index] is None:
                return "The entry has been deleted!"
            elif self.__storage[index].secret:
                return None
            else:
                raise TypeError("The index must be format str!")
        except IndexError:
            return 'There is no such index!'

    # Changing information about the info of the archive
    def set_info(self, index, new_info):
        self.__storage[index].set_info(new_info)

    # Classify information
    def classify(self, index):
        self.__storage[index].classify()

    # Declassify information
    def declassify(self, index):
        self.__storage[index].declassify()

    # Delete information
    def delete(self, index):
        self.__storage[index] = None


class Entry:
    def __init__(self, item, date="01.01.1970", info="", secret=False):
        self.__id = self.__get_next_id()
        self.__item = item
        self.__date = date
        self.__info = info
        self.__secret = secret

    # Getting information about the id of the Entry
    @property
    def id(self):
        if type(self.__id) == int:
            return self.__id
        else:
            raise TypeError("The id must be format int!")

    # Getting information about the item of the Entry
    @property
    def item(self):
        return self.__item

    # Getting information about the date of the Entry
    @property
    def date(self):
        if type(self.__date) == str:
            return self.__date
        else:
            raise TypeError("The date must be format str!")

    # Getting information about the info of the Entry
    @property
    def info(self):
        return self.__info

    # Getting information about the secret of the Entry
    @property
    def secret(self):
        return self.__secret

    # Changing information about the info of the Entry
    def set_info(self, new_info):
        self.__info = new_info

    # Classify information
    def classify(self):
        self.__secret = True

    # Declassify information
    def declassify(self):
        self.__secret = False

    def __get_next_id(self):
        return hash(self)


# Cannot be deleted!
name_of_archive = Archive()
