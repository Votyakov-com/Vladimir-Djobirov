import matplotlib.pyplot as plt

import numpy as np

languages_of_programming = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
rating = [22, 18, 9, 8, 7, 6]

fig, ax = plt.subplots(nrows=1, ncols=1)
plt.title("Популярность языков программирования")
ax.bar("Java", np.arange(0, 21), color='r')
ax.bar("Python", np.arange(0, 19), color='black')
ax.bar("PHP", np.arange(0, 10), color='green')
ax.bar("JavaScript", np.arange(0, 9), color='blue')
ax.bar("C#", np.arange(0, 8), color='yellow')
ax.bar("C++", np.arange(0, 7))
plt.grid(True, linewidth=0.5, alpha=0.5)
plt.xlabel("Языки программирования")
plt.ylabel("Популярность")

plt.show()