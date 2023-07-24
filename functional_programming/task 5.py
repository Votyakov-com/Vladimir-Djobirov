from functools import reduce


def reduce_sum(numbers):
    return reduce((lambda number_current, number_next: number_current + number_next), numbers)
