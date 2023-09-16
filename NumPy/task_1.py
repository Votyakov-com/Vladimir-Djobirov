from random import randint

import numpy as np

rng = np.random.default_rng()

array = rng.integers(low=1, high=11, size=(randint(1, 10), randint(1, 10)))
max_values = array.max(axis=0)
