"""Вам необходимо реализовать функцию length_frequencies(), которая принимает последовательность (iterable) слов (строк) в качестве единственного аргумента и возвращает словарь, ключами которого выступают длины слов, а значениями — количество слов соответствующей длины.

>>> from solution import length_frequencies
>>> length_frequencies([])
{}
>>> length_frequencies(['abcde'])
{5: 1}
>>> length_frequencies(['a', 'b', 'c'])
{1: 3}
>>> length_frequencies('Use the Force, Luke!'.split())
{3: 2, 5: 1, 6: 1}
>>>
Это задание можно выполнить в процедурном стиле с помощью defaultdict или dict.setdefault, однако попробуйте описать декларативное решение с использованием comprehensions. Возможно, вам пригодится функция itertools.groupby()."""

# BEGIN
from itertools import groupby


def count(sequence):
    return sum(1 for _ in sequence)


def length_frequencies(words):
    return {
        length: count(group)
        for length, group in groupby(sorted(
            len(word) for word in words
        ))
    }
# END