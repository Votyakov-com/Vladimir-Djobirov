import matplotlib.pyplot as plt

import numpy as np

goals = [2, 3, 1, 4, 2]
miss = [1, 2, 0, 3, 1]

x = np.arange(1, 6)
width = 0.3

fig, ax = plt.subplots()
plt.title("Результаты матчей")
ax.bar(x, goals, width=width, label="Забитые гола")
ax.bar(x - width, miss, width=width, label="Пропущенные гола")
plt.xlabel('Номер матча')
plt.ylabel('Количество забитых голов')
plt.legend()
plt.show()
