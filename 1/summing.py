def sum_numbers(numbers=None):
    if not numbers and not(isinstance(numbers, list)):
        return sum(list(range(1,101)))

    return sum(numbers)

