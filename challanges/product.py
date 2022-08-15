"""Вам предстоит реализовать функцию product(), которая принимает один и более позиционных параметров — iterable любого вида, и возвращает список кортежей. Возвращаемый список представляет собой декартово произведение элементов входных последовательностей — все сочетания "каждый с каждым". Например, для последовательностей [1, 2] и 'ab' (помним, строки — тоже iterable) функция должна вернуть список [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')], то есть каждый элемент списка с каждым символом строки.

>>> from solution import product
>>> product()  # хотя бы одна последовательность должна быть дана
Traceback (most recent call last):
   ...
TypeError: product() missing 1 required positional argument: 'sequence'
>>> product([])
[]
>>> product([1, 2], 'abc')
[(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]
>>> product('hello', [], 'world')
[]
>>> # ^ если хотя бы одна из входных последовательностей пустая,
>>> # то выходной список тоже будет пуст
>>>"""

def product(sequence, *args):
    subproducts = product(*args) if args else [()]
    # ^ произведение оставшихся последовательностей вычисляем заранее
    # чтобы не строить заново для каждого элемента первой последовательности
    return [
        (first,) + subproduct
        for first in sequence
        for subproduct in subproducts
    ]
# END

# BEGIN (write your solution here)
def product_gen(sequence, *args):
    if sequence:
        for a in sequence:
            for prod in product(*args) if args else ((),):
                yield (a,) + prod


def product_2(sequence, *args):
    return list(product_gen(sequence, *args))
# END