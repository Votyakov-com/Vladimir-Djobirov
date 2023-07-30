import copy
import random


class Revolver:
    def __init__(self, indicator, revolver_drum=[], ):
        self.revolver_drum = revolver_drum
        try:
            self.indicator = random.choice(
                [bullet for bullet in [0, 1, 2, 3, 4, 5] if self.revolver_drum[bullet] == True])
        except IndexError:
            print('Кажется возникла ошибка :(')

    def add_bulet(self):
        if self.revolver_drum[0] == 0:
            self.revolver_drum[0] = 1
            return f'Патрон успешно добавлен: [{True}]'
        elif self.revolver_drum[1] == 0:
            self.revolver_drum[1] = 1
            return f'Патрон успешно добавлен: [{True}]'
        elif self.revolver_drum[2] == 0:
            self.revolver_drum[2] = 1
            return f'Патрон успешно добавлен: [{True}]'
        elif self.revolver_drum[3] == 0:
            self.revolver_drum[3] = 1
            return f'Патрон успешно добавлен: [{True}]'
        elif self.revolver_drum[4] == 0:
            self.revolver_drum[4] = 1
            return f'Патрон успешно добавлен: [{True}]'
        elif self.revolver_drum[5] == 0:
            self.revolver_drum[5] = 1
            return f'Патрон успешно добавлен: [{True}]'
        else:
            return f'Револьвер итак полностью заряжен!'

    def add_bullets_from_list(self, List):
        copy_revolver_drum_num_1 = copy.deepcopy(self.revolver_drum)

        if sum(self.revolver_drum) == 6:
            return f'Револьвер итак полностью заряжен!'
        else:
            for i in range(min(len(List), len(self.revolver_drum))):
                self.revolver_drum[i] = List[i]
            if copy_revolver_drum_num_1 == self.revolver_drum:
                return f'Данные слоты итак заряжены, вывожу: [{False}]'
            else:
                return f'Все патроны успешно добавлены [{True}]'

    def shoot(self):
        if self.revolver_drum[self.indicator] == 1:
            self.revolver_drum[self.indicator] = 0
            if self.indicator == 5:
                self.indicator == 0
            else:
                self.indicator += 1
            return f'Патрон успешно удален [{True}]'
        else:
            return f'В данном индексе итак нет патрона, нечего удалать. Вывожу: [{False}]'

    def unload(self):
        if sum(self.revolver_drum) == 0:
            return f'В барабане итак нет патронов, посмотри сам {self.revolver_drum}'
        else:
            copy_revolver_drum_num_2 = copy.deepcopy(self.revolver_drum)
            self.revolver_drum = [0, 0, 0, 0, 0, 0]
            return f'Все патроны извлечены: {copy_revolver_drum_num_2} --> {self.revolver_drum}'

    def scroll(self):
        self.indicator = random.choice([0, 1, 2, 3, 4, 5])

    def bullet_count(self):
        return f'Количество патронов: {sum(self.revolver_drum)}'
