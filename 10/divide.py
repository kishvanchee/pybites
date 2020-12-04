def positive_divide(numerator, denominator):
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        raise TypeError

    try:

        x = numerator / denominator

        if x < 0:
            raise ValueError

        return x

    except ZeroDivisionError:
        return 0
