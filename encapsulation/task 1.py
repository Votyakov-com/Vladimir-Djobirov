from random import *


class CRM:
    def __init__(self):
        self.__abiturients = {}

    def add(self, abiturient):
        # Getting number
        number = abiturient.get_number()

        # adding an entrant to the dictionary
        # where information is stored under numbers
        self.__abiturients[number] = abiturient

    def get_status(self, number):
        abiturient = self.__abiturients.get(number)
        if abiturient is None:
            return "Entrant is not defined"
        return abiturient.get_status()


class Abiturient:
    def __init__(self, name, surname, patronymic, age, number, bvi=False):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age

        # number
        self.__number = number

        # Russian National Exam (ЕГЭ), balls
        self.__rne = self.__fetch_rne()

        # have BVI ?
        self.__bvi = bvi

    # function getting results EGE
    def __fetch_rne(self):
        return tuple(randint(0, 100) for _ in range(3))

    # function answer on question, does the applicant pass
    def __check(self):
        if self.__bvi:
            return "Да"
        if random() > 0.95:
            return "Да"
        return "Нет"

    # information received about the applicant's full name
    @property
    def nsp(self):
        return self.__name, self.__surname, self.__patronymic

    # changing information about the applicant's full name
    @nsp.setter
    def nsp(self, value):
        self.__name, self.__surname, self.__patronymic = value

    # Getting information about the age of the entrant
    @property
    def age(self):
        return self.__age

    # Changing information about the age of the entrant
    @age.setter
    def age(self, age):
        self.__age = age

    # Getting information about the results RNE
    @property
    def rne(self):
        return self.__rne

    # Changing information about the results RNE
    @rne.setter
    def rne(self, value):
        self.__rne = list(self.__rne)
        self.__rne[0], self.__rne[1], self.__rne[2] = value
        self.__rne = tuple(self.__rne)

    # Getting information about the status BVI of the entrant
    @property
    def bvi(self):
        return self.__bvi

    # Changing information about the status BVI of the entrant
    @bvi.setter
    def bvi(self, status_bvi):
        self.__bvi = status_bvi

    def get_number(self):
        return self.__number

    def get_status(self):
        if self.__bvi:
            return "Congratulations, you pass!"
        if random() > 0.95:
            return "Congratulations, you pass!"
        return "At the moment you are not passing!"


# Cannot be deleted!
module = CRM()
