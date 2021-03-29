def freq_digit(num: int) -> int:
    from collections import Counter
    return int(Counter(str(num)).most_common(1)[0][0])
