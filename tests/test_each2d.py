from lessons.each2d import each2d, some2d, sum2d


def anything(_):
    return True


def is_positive(x):
    return x > 0


BOOM = object()


def non_boom(check):
    """Wait for the BOOM value and applies the check to non-BOOMs."""
    def inner(x):
        assert x is not BOOM, "Your code shouldn't reach this point!"
        return check(x)
    return inner


def test_each2d():
    assert each2d(anything, []) is True, (
        "In empty matrix there is nothing to fail the test!"
    )
    assert each2d(anything, [[]]) is True, (
        "In empty matrix there is nothing to fail the test!"
    )
    assert each2d(non_boom(is_positive), [
        [1, 2, 3],
        [4, 0, BOOM],  # your code should stop at 0
        [7, 8, 9],
    ]) is False


def test_some2d():
    assert some2d(anything, []) is False, (
        "In empty matrix there is nothing to pass the test!"
    )
    assert some2d(anything, [[]]) is False, (
        "In empty matrix there is nothing to pass the test!"
    )

    assert some2d(non_boom(is_positive), [
        [0, -1, -10],
        [-5, 2, BOOM],  # your code should stop at 2
        [4, 5, 6],
    ]) is True


def test_sum2d():
    assert sum2d(anything, []) == 0, (
        "In empty matrix there is nothing to sum!"
    )

    assert sum2d(anything, [[1, 2, 3], [4, 5, 6]]) == 21

    assert sum2d(is_positive, [[-1, 2, -3], [4, -5, 6]]) == 12