import matplotlib.pyplot as plt

import numpy as np

x = np.arange(0,51, 10)
y = x * 3

plt.plot(x, y)
plt.title("Нарисуй линию")
plt.xlabel("Ось x")
plt.ylabel("Ось y")
plt.xticks(np.linspace(0, 50, 6))
plt.yticks(np.linspace(0, 140, 8))
plt.show()