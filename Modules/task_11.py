import math
import random

import imp_modules

imp_modules.imp_mods(['math', 'random'])
print(math.factorial(random.randint(0, 10)))
