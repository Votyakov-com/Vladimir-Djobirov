from random import randint

import numpy as np


def dot():
    rng = np.random.default_rng()
    size = (randint(1, 10), randint(1, 10))
    array = rng.integers(low=1, high=100, size=size)

    dictionary_of_dots = dict()

    for i in range(size[0]):
        min_height = array[i].min()
        count = np.count_nonzero(array == min_height)
        dictionary_of_dots[str(min_height)] = count

    print("Array:")
    print(array)
    print("Dictionary of Dots:")
    print(dictionary_of_dots)


dot()
