import random


class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self):
        print('Интересный вопрос, давайте разбираться вместе!')


class Teacher(Human):
    def __init__(self, name):
        super().__init__(name)


class Mentor(Human):
    def __init__(self, name):
        super().__init__(name)


class CodeReviewer(Human):
    def __init__(self, name):
        super().__init__(name)


class Curator(Human):
    def __init__(self, name):
        super().__init__(name)


class Student(Human):
    def __init__(self, name):
        super().__init__(name)

    def ask_question(self, human, question):
        quest = f'{human.name}, {question.lower()}'
        print(quest)
        if isinstance(human, Teacher):
            array_of_question = ['Сейчас расскажу', 'Хороший вопрос, ща все поясню',
                                 'Тут дело в 3 вещах...',
                                 'Понял, сейчас постараюсь объяснить']
            print(random.choice(array_of_question) + '\n')
        if isinstance(human, Mentor):
            array_of_question = ['У меня тоже такое было...Главное не волнуйся',
                                 'Тут важно соблюдать три правила!',
                                 'Подожди секунду, сейчас обращусь к составителям']
            print(random.choice(array_of_question) + '\n')
        if isinstance(human, Curator):
            array_of_question = ['Сейчас опишу ход мыслей при решении задачи.',
                                 'В этом случае вам следовало бы поступить следующим образом',
                                 'Попробую подсказать ход правильного решения']
            print(random.choice(array_of_question) + '\n')
        if isinstance(human, CodeReviewer):
            array_of_question = ['Проверил, нестандартное мышление тоже хорошо! Умница!',
                                 'Неплохой способ, проверено! Молодец!',
                                 'Проверил, код читабелен, что в принципе и нужно! Продолжай в том же духе!']
            print(random.choice(array_of_question) + '\n')
