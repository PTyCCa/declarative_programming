from itertools import islice

from challanges.intersperse import intersperse


def test_intersperse():
    assert list(intersperse([], ",")) == []
    assert list(intersperse([42], "foo")) == [42]
    assert "".join(intersperse(["Hello", "World"], " ")) == "Hello World"
    assert list(intersperse(range(4), 0)) == [0, 0, 1, 0, 2, 0, 3]


def test_intersperse_laziness():
    # Эта функция-генератор помнит, сколько было итераций когда либо
    def indicator():
        while True:
            indicator.count += 1
            yield "click"
    indicator.count = 0

    clicks = intersperse(indicator(), ",")
    assert indicator.count == 0, "No iterations should be performed yet!"

    first_ten = islice(clicks, 10)
    assert list(islice(first_ten, 3)) == ["click", ",", "click"]
    assert indicator.count == 2, "There are should be just two iterations!"
