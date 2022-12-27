import t

def test_sum():
    result = t.sum(1, 2)
    expected = 3
    assert result == expected


def test_multiply():
    result = t.multiply(1, 2)
    expected = 2
    assert result == expected

