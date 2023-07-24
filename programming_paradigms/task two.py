from functools import reduce

numbers = [14, 93, 19, 38, 18, 51, 77]


def sum_even_numbers(numbers):
    array_of_even = list(filter((lambda x: x % 2 == 0), numbers))
    summa = reduce((lambda x, y: x + y), array_of_even)
    return summa


print(sum_even_numbers(numbers))
