from lessons.unique_letters import number_of_unique_letters


def test_number_of_unique_letters():
    assert number_of_unique_letters("") == 0
    assert number_of_unique_letters("Aa") == 1
    assert number_of_unique_letters("a,b_C  \nd") == 4
    assert number_of_unique_letters("number_of_unique_letters") == 13
