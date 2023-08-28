import statistics
# from statistics import * - Not used!
import statistics as library_statistics
from statistics import mean
from statistics import mean as function_mean

print(statistics.mean([1, 2, 3]))  # Вывод: 2
print(mean([1, 2, 3]))  # Вывод: 2
print(mean([1, 2, 3]))  # Вывод: 2
print(function_mean([1, 2, 3]))  # Вывод: 2
print(library_statistics.mean([1, 2, 3]))  # Вывод: 2
