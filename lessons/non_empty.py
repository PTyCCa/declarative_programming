"""Вам предстоит написать функцию non_empty_truths(), которая с помощью генераторов списков должна вычислять копию входного списка списков, "очищенную" от ложных элементов (не только False, а любых ложных!), а заодно и от пустых списков — таковые могу присутствовать сами по себе или могут получаться после отбрасывания из них всех элементов.

Выглядеть использование полученной функции должно так:

>>> from solution import non_empty_truths
>>> non_empty_truths([])  # нечего отбрасывать, это тоже нормально
[]
>>> non_empty_truths([[], []])  # пустые отбрасываем
[]
>>> non_empty_truths([[0]])  # чистим, чистые, но пустые тоже отбрасываем
[]
>>> non_empty_truths([[0, ""], [False, None]])  # в Python многое считается ложным
[]
>>> non_empty_truths([[0, 1, 2], [], [], [False, True, 42]])
[[1, 2], [True, 42]]
>>>"""

# BEGIN
def non_empty_truths(list_of_lists):
    return [
        truths for truths in
        [[elem for elem in one_list if elem]  # noqa: WPS335
         for one_list in list_of_lists
         ]
        if truths
    ]
# END

# def non_empty_truths(some_list):
#     [truths for truths in [[elem for elem in one_list if elem]
#     for one_list in list_of_lists] if truths]
# END