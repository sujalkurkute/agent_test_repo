from buggy_math import add_numbers

def test_add_numbers():
    result = add_numbers(2, 3)
    assert isinstance(result, str)
