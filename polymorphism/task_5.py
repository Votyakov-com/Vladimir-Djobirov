from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def vote_command(self):
        pass

    @abstractmethod
    def gesture_command(self):
        pass


class Lock(ABC):
    @abstractmethod
    def close_lock(self):
        pass

    @abstractmethod
    def open_lock(self):
        pass


class SmartAssistant(Command):
    def vote_command(self):
        print('Умный помощник распознал голосовую команду' + '\n')

    def gesture_command(self):
        print('Умный помощник распознал жестовые команды' + '\n')


class SmartCamera(Command, Lock):
    def open_lock(self):
        print('Умная камера открыла замок входной двери' + '\n')

    def close_lock(self):
        print('Умная кампра закрыла замок входной двери' + '\n')

    def vote_command(self):
        print('Умный помощник распознал голосовую команду' + '\n')

    def gesture_command(self):
        print('Умный помощник распознал жестовые команды' + '\n')


class SmartLock(Lock):
    def close_lock(self):
        print('Умная камера закрыла замок входной двери' + '\n')

    def open_lock(self):
        print('Умная камера открыла замок входной двери' + '\n')
