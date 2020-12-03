def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    import string
    return ''.join((s for s in input_string if s not in string.punctuation))
