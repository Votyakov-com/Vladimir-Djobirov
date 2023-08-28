from abc import ABC, abstractmethod


class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Crow(Walkable, Flyable):
    def walk(self):
        pass

    def fly(self):
        pass

    def swim(self):
        raise NotImplementedError('Вороны не умеют плавать!')


class Penguin(Walkable, Swimmable):
    def walk(self):
        pass

    def swim(self):
        pass

    def fly(self):
        raise NotImplementedError('Пингвины не умеют летать!')
