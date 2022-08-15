from challanges.lenght_frequency import length_frequencies


def test_length_frequencies():
    assert isinstance(length_frequencies([]), dict), (
        "Function should return a dict"
    )
    assert length_frequencies([]) == {}
    assert length_frequencies(["a", "bb", "ccc"]) == {1: 1, 2: 1, 3: 1}
    assert length_frequencies(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.""".split(),
    ) == {
        2: 13,
        3: 5,
        4: 9,
        5: 12,
        6: 7,
        7: 9,
        8: 3,
        9: 5,
        10: 3,
        11: 1,
        12: 1,
        13: 1,
    }