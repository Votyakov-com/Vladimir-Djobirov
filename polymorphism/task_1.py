from abc import ABC, abstractmethod


class Book(ABC):
    @abstractmethod
    def display(self):
        pass


class Autobiography(Book):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в '
              f'автобиографическом жанре. Автор - {self.author}')


class Psychology(Book):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в '
              f'жанре психологии. Автор - {self.author}')


class Fantasy:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в '
              f'жанре фэнтези. Автор - {self.author}')
