from types import GeneratorType

from lessons.my_map import my_filter, my_map, replicate_each


def make_trigger():
    state = []
    return (
        lambda: bool(state),
        lambda *args: state.append(True),
    )


def test_my_map():
    assert isinstance(my_map(abs, []), GeneratorType), (
        "my_map should be a generator function",
    )
    assert list(my_map(abs, (x for x in ''))) == []
    assert list(my_map(abs, [-1, 2, -3])) == [1, 2, 3]


def test_my_map_laziness():
    is_called, callback = make_trigger()
    my_map(callback, [1, 2, 3])
    assert not is_called(), "my_map shouln't apply the function before next()"


def test_my_filter():
    assert isinstance(my_filter(bool, []), GeneratorType), (
        "my_filter should be a generator function",
    )
    assert list(my_filter(bool, (x for x in ''))) == []
    assert list(my_filter(bool, [0, 1, 'a', ''])) == [1, 'a']


def test_my_filter_laziness():
    is_called, callback = make_trigger()
    my_filter(callback, [1, 2, 3])
    assert not is_called(), (
        "my_filter shouln't apply the function before next()"
    )


def test_replicate_each():
    assert isinstance(replicate_each(0, []), GeneratorType), (
        "replicate_each should be a generator function",
    )
    assert list(replicate_each(0, [1, 2, 3])) == []
    assert list(replicate_each(1, [1, 2, 3])) == [1, 2, 3]
    assert list(replicate_each(3, [1, 'a'])) == [1, 1, 1, 'a', 'a', 'a']