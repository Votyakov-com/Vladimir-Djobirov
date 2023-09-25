import matplotlib.pyplot as plt

import numpy as np

x = np.array(["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"])
y = np.array([25, 28, 39, 27, 22, 24, 26])

plt.plot(x, y)
plt.title("График измерение температур")
plt.xlabel("Дни недели")
plt.ylabel("Градусы Цельсия")
plt.grid()
plt.show()
