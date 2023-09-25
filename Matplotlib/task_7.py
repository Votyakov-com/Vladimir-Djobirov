import matplotlib.pyplot as plt

import numpy as np

days = [0, 1, 2, 3, 4]
visits_1 = [50, 60, 70, 80, 90]
visits_2 = [40, 55, 75, 85, 95]

fig, ax = plt.subplots(1, 2)
ax[0].plot(days, visits_1)
ax[0].set_title("Посещения сайта A")
ax[0].set_xlabel("День")
ax[0].set_ylabel("Количество посещений")
ax[1].plot(days, visits_2)
ax[1].set_title("Посещения сайта B")
ax[1].set_xlabel("День")
ax[1].set_ylabel("Количество посещений")
plt.xticks(np.arange(1, 5))
plt.tight_layout()  # Оптимизация местоположения графиков
plt.show()
