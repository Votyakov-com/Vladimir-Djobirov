from random import choice as chc
from random import randint as rnd

array = list(map((lambda number: rnd(1, 100)), [0] * 10))
print(array)
print(chc(array))
