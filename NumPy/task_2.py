from random import randint

import numpy as np

rng = np.random.default_rng()
size = (randint(1, 10), randint(1, 10))

array = rng.integers(low=1, high=11, size=size)
average_grades = [np.mean(array[i]) for i in range(size[0])]
