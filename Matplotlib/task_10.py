import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
x = np.random.normal(-1, 1, 1000)
y = np.random.normal(-1, 1, 1000)

plt.scatter(x, y, color="red", s=2)
plt.show()
