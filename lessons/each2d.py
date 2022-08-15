"""Вам предстоит реализовать три функции, каждая из которых будет работать с двухмерной матрицей, то есть со списком списков (итератором итераторов).

each2d(test, matrix) должна проверить, что каждый элемент матрицы matrix удовлетворяет предикату test, и вернуть False, если хотя бы для одного элемента test вернул False. В противном случае функция должна возвращать True.
some2d(test, matrix) должна проверить, удовлетворяет ли предикату test хотя бы один элемент матрицы matrix. Как только test возвращает True для какого-либо элемента, функция должна вернуть True, в противном случае (если ни один элемент проверку не прошёл) нужно вернуть False.
sum2d(test, matrix) должна возвращать сумму всех элементов матрицы matrix, удовлетворяющих предикату test.
Внимание, первые две функции не должны выполнять лишней работы: обход матрицы должен прерываться, как только результат становится ясен.

>>> from solution import each2d, some2d, sum2d
>>> def is_int(x):
...     return isinstance(x, int)
...
>>> each2d(is_int, [[1, 2], [3, 4]])
True
>>> each2d(is_int, [[1, None], [3, 4]])
False
>>> # В пустой матрице нет ни одного элемента, который бы завалил тест
>>> each2d(is_int, [])
True
>>> some2d(is_int, [[None, "foo"], [(), {}]])
False
>>> some2d(is_int, [[None, "foo"], [0, {}]])
True
>>> # В пустой матрице нет ни одного элемента, который бы прошёл тест
>>> some2d(is_int, [])
False
>>> sum2d(is_int, [[1, "Foo", 100], [False, 10, None]])
111
>>>"""

# BEGIN
def each2d(test, matrix):
    return all(
        all(test(cell) for cell in row)
        for row in matrix
    )


def some2d(test, matrix):
    return any(
        any(test(cell) for cell in row)
        for row in matrix
    )


def sum2d(test, matrix):
    return sum(
        sum(cell for cell in row if test(cell))
        for row in matrix
    )
# END