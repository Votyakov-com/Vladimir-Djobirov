from functools import reduce


def add(*args):
    if len(args) < 2:
        print('Недостаточно элементов!')
    else:
        print(sum(args))


def subtract(*args):
    if len(args) < 2:
        print('Недостаточно элементов!')
    else:
        print(args[0] - sum(args[1:]))


def multiply(*args):
    if len(args) < 2:
        print('Недостаточно элементов!')
    else:
        print(reduce((lambda number_one, number_two: number_one * number_two), args))


def divide(*args):
    if len(args) < 2:
        print('Недостаточно элементов!')
    else:
        print(reduce((lambda number_one, number_two: number_one / number_two), args))
