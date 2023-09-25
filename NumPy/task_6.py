from random import randint

import numpy as np

rng = np.random.default_rng()
random_number = randint(1, 10)
size = (random_number, random_number)
array = rng.integers(low=1, high=10, size=size)


def magic_square(ar):
    all_lines_are_equal = all(sum(ar[i]) == sum(ar[i + 1]) for i in range(len(ar) - 1))
    summ_of_columns = [sum(column) for column in zip(*ar)]
    all_columns_are_equal = len(set(summ_of_columns)) == 1

    if all_columns_are_equal and all_lines_are_equal:
        print('It\'s a Magic Square!')
    else:
        print('No')


magic_square(array)
