from importlib import import_module


def imp_mods(mods):
    try:
        for m in mods:
            m = import_module(m)
            print(f'Модуль {m} успешно импортирован!')
    except ModuleNotFoundError:
        print('Кажется какой-то модуль не найден!')


imp_mods(['random', 'math', 'time'])