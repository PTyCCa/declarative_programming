from collections import defaultdict
from itertools import islice

from challanges.round_robin import round_robin


def test_round_robin():
    assert list(round_robin()) == [], "It should be ok to have no sources!"

    assert list(round_robin(range(10))) == list(range(10))

    assert list(round_robin("ab", "QWE")) == ["a", "Q", "b", "W", "E"], (
        "Function should work fine with sources those aren't equal by length!"
    )

    assert list(round_robin("JKL", [])) == ["J", "K", "L"], (
        "Any source can be empty!"
    )

    one = iter(range(20))
    two = one  # две ссылки на один итератор!
    assert list(round_robin(one, two)) == list(range(20))

    assert list(round_robin(
        [1, 2, 3],
        "ab",
        [100, 200, 300],
    )) == [1, 'a', 100, 2, 'b', 200, 3, 300]


def test_round_robin_laziness():
    counters = defaultdict(int)

    def tick_as(name):
        while True:
            counters[name] += 1
            yield name

    k1, k2, k3 = "abc"
    queue = iter(round_robin(
        tick_as(k1),
        tick_as(k2),
        tick_as(k3),
    ))
    assert counters == {}, "No iterators should be touched yet!"

    assert (next(queue), next(queue)) == (k1, k2)
    assert counters == {k1: 1, k2: 1}, "Third source shouldn't be touched yet!"

    assert "".join(islice(queue, 8)) == "cabcabca"
    assert counters == {k1: 4, k2: 3, k3: 3}