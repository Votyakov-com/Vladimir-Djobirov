import matplotlib.pyplot as plt

import numpy as np

labels = np.array(["Рок", "Поп", "Хип-Хоп", "Электронная", "Классическая"])
vals = np.array([30, 20, 15, 10, 25])

plt.title("Популярность музыки")
plt.pie(vals, labels=labels)
plt.show()
