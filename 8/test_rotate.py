from rotate import rotate


def test_small_rotate():
    assert rotate('hello', 2) == 'llohe'
    assert rotate('hello', -2) == 'lohel'


def test_bigger_rotation_of_positive_n():
    string = 'bob and julian love pybites!'
    expected = 'love pybites!bob and julian '
    assert rotate(string, 15) == expected


def test_bigger_rotation_of_negative_n():
    string = 'pybites loves julian and bob!'
    expected = 'julian and bob!pybites loves '
    assert rotate(string, -15) == expected


def test_rotation_of_n_same_as_len_str():
    string = expected = 'julian and bob!'
    assert rotate(string, len(string)) == expected


def test_rotation_of_n_bigger_than_string():
    string = expected = 'julian and bob!'
    assert rotate(string, 100) == expected