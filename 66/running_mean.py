def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    import itertools
    sums = itertools.accumulate(sequence)
    return (round(s / i, 2) for i, s in enumerate(sums, 1))
