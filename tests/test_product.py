import pytest

from challanges.product import product


def test_product_on_simple_cases():
    assert isinstance(product([]), list), "Function should return a list."
    assert product([]) == []
    assert product('q') == [('q',)], "Should work with strings!"
    assert product('abc') == [('a',), ('b',), ('c',)]


def test_product_on_complex_cases():
    assert product('foo', [1, 2, 3], '') == []
    assert product('A', 'B') == [('A', 'B')]
    assert product([0, 1], [2, 3], [4, 5]) == [
        (0, 2, 4),
        (0, 2, 5),
        (0, 3, 4),
        (0, 3, 5),
        (1, 2, 4),
        (1, 2, 5),
        (1, 3, 4),
        (1, 3, 5),
    ]


def test_product_on_zero_args():
    with pytest.raises(
        TypeError,
        match='missing 1 required positional argument',
    ):
        product()