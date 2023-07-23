numbers = [60, 84, 9, 49, 7, 85, 38]


def sum_even_numbers(numbers):
    summa = 0
    for number in numbers:
        if number % 2 == 0:
            summa += number
    return summa


print(sum_even_numbers(numbers))
