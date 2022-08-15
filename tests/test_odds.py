from lessons.odds import keep_odds_from_odds, odds_from_odds


def test_odds_from_odds_on_empty_input():
    assert odds_from_odds([]) == [], "Function should work with empty lists!"
    assert odds_from_odds([[]]) == [[]], "Lists in list can be empty!"


def test_odds_from_odds():
    argument = [
        [1, 2, 3, 4, 5],
        ['c', 'a', 't'],
        ['d', 'o', 'g'],
        [100, 200, 300, 400],
        [True, False],
        [],
        [],
    ]
    backup = list(map(lambda x: x[:], argument))  # a deep copy

    selection = odds_from_odds(argument)
    assert argument == backup, "Original list shouldn't be changed!"
    assert selection == [
        [1, 3, 5],
        ['d', 'g'],
        [True],
        [],
    ]


def test_keep_odds_from_odds_empty_input():
    assert keep_odds_from_odds([]) is None, (
        "Procedure should work with empty lists!"
    )
    assert keep_odds_from_odds([[]]) is None, "Lists in list can be empty!"


def test_keep_odds_from_odds():
    argument = [
        [1, 2, 3, 4, 5],
        ['c', 'a', 't'],
        ['d', 'o', 'g'],
        [100, 200, 300, 400],
        [True, False],
        [],
        [],
    ]

    assert keep_odds_from_odds(argument) is None, (
        "Procedure shouldn't return anything!"
    )
    assert argument == [
        [1, 3, 5],
        ['d', 'g'],
        [True],
        [],
    ]

    keep_odds_from_odds(argument)
    assert argument == [
        [1, 5],
        [True],
    ]

    keep_odds_from_odds(argument)
    assert argument == [[1]]

    keep_odds_from_odds(argument)
    assert argument == [[1]]


def test_keep_odds_from_odds_with_doubles():
    # Этот тест проверяет, что процедура удаляет элементы
    # именно по индексу, а не по равенству значений.

    argument = [[1, 2, 3, 1, 5]]

    keep_odds_from_odds(argument)
    assert argument == [[1, 3, 5]]

    argument = [[1], [2], [3], [1], [5]]

    keep_odds_from_odds(argument)
    assert argument == [[1], [3], [5]]