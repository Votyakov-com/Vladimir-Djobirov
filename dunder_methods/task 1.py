signature = "-~=$([{VLADIMIR}])$=~-"


class SignedMessage:

    def __init__(self, message, signature):
        self.message = message
        self.signature = signature
        self.infiltrate()

    def __str__(self):
        return f'{self.message} {self.signature}'

    def __add__(self, other, a):
        return f'{self.message} {other.message} {self.signature}'

    def infiltrate(self):
        pass