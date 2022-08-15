"""Вам предстоит реализовать функцию intersperse(), которая должна принимать два аргумента: итерируемый источник значений и значение-разделитель. Функция должна возвращать такой итератор, который "между" соседними значениями из источника отдавал бы значение разделитель. Помните, что

ваша функция должна возвращать именно итератор;
ни один элемент из входного итератора не должен быть получен, пока это значение не потребуют от результирующего итератора (если вообще потребуют!);
результирующий итератор не должен вставлять разделитель следом за последним элементом входного потока.
>>> from solution import intersperse
>>> list(intersperse([], ","))
[]
>>> list(intersperse([42], "foo"))
[42]
>>> "".join(intersperse(["Hello", "World"], " "))
'Hello World'
>>> list(intersperse(range(4), 0))
[0, 0, 1, 0, 2, 0, 3]
>>>"""

# BEGIN
def intersperse(source, separator):
    cursor = iter(source)
    for first_item in cursor:
        yield first_item
        break
    for next_item in cursor:
        yield separator
        yield next_item  # noqa: WPS354
        # Замечание WPS354 можно было бы подавить, написав
        # "yield from (separator, next_item)",
        # но такой код читается сложнее
# END