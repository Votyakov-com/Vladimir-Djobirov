import matplotlib.pyplot as plt

x1 = [10, 15, 20, 30]
y1 = [20, 30, 40, 10]

x2 = [10, 20, 30]
y2 = [40, 10, 30]

fig, ax = plt.subplots()
plt.title("Нарисуй график")
graf1 = ax.plot(x1, y1, label="Линия 1")
graf2 = ax.plot(x2, y2, label="Линия 2")
plt.xlabel("Ось x")
plt.ylabel("Ось y")
plt.legend()
plt.show()
