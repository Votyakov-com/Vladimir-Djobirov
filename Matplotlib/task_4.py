import matplotlib.pyplot as plt

fruits = ["Яблоки", "Груши", "Бананы", "Апельсины", "Персики"]
amount = [100, 85, 70, 60, 45]

plt.figure(figsize=(12, 5))
plt.rcParams.update({'font.size': 17})
plt.title("Данные о продажах фруктов")
plt.barh(fruits, amount, color="y")
plt.grid()
plt.show()
