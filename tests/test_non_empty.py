from lessons.non_empty import non_empty_truths


def test_non_empty_truths():
    assert non_empty_truths([]) == []
    assert non_empty_truths([[], [], []]) == []
    assert non_empty_truths([[], [1], [], [2]]) == [[1], [2]]
    assert non_empty_truths([[0, ""], [False, None]]) == []
    assert non_empty_truths([[1, 0, -1], [True, False]]) == [[1, -1], [True]]
