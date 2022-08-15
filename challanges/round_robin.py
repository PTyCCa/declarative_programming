"""Вам предстоит реализовать функцию, выполняющую роль балансировщика очередей. Функция должна принимать произвольное количество аргументов-iterable и возвращать новый iterable. Возвращаемый iterable должен выдавать значения по одному из каждой не пустой очереди (аргумента) и переходить к следующей очереди по кругу, пока все очереди не опустеют. Переходить от очереди к очереди следует в том порядке, в котором аргументы были переданы в функцию.

>>> from solution import round_robin
>>> list(round_robin())  # аргументов может и не быть!
[]
>>> # входные очереди могут быть разной длины
>>> list(round_robin("ab", "QWE"))
['a', 'Q', 'b', 'W', 'E']
>>> # очередь должна быть ленивой
>>> # ведь любой источник может быть бесконечным, как count()
>>> from itertools import islice, count
>>> list(islice(round_robin(count(), "abc"), 10))
[0, 'a', 1, 'b', 2, 'c', 3, 4, 5, 6]
>>>"""

# BEGIN

# В этом модуле линтер ругается на cognitive complexity, но в данном случае
# и сама по себе задача — сложная. Поэтому игнорируем предупреждения :)
# flake8: noqa

from itertools import cycle


def round_robin(*args):
    sources = [
        (index, iter(source))
        for index, source in enumerate(args)
    ]
    rest_sources = {index for index, _ in sources}
    for index, source in cycle(sources):
        if index in rest_sources:
            for next_value in source:
                yield next_value
                break
            else:
                rest_sources.remove(index)
        if not rest_sources:
            break
# END

# BEGIN (write your solution here)
from itertools import cycle, islice


def round_robin_2(*args):
    num_active = len(args)
    nexts = cycle(iter(item).__next__ for item in args)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))
# END