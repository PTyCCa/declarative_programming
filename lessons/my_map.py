"""Вам предстоит потренироваться в написании генераторных функций и написать три штуки:

my_map(f, xs), которая должна работать как упрощённая версия map()
my_filter(f, xs), упрощённый вариант filter()
replicate_each(n, xs) должен для каждого элемента итератора xs выдавать на выход по n копий этого элемента
>>> from solution import my_map, my_filter, replicate_each
>>> list(my_map(abs, [-1, 2, -3]))
[1, 2, 3]
>>> list(my_filter(lambda x: x % 2 == 1, range(10)))
[1, 3, 5, 7, 9]
>>> list(replicate_each(1, [1, 'a']))
[1, 'a']
>>> list(replicate_each(3, [1, 'a']))
[1, 1, 1, 'a', 'a', 'a']
>>> list(replicate_each(0, [1, 'a']))
[]
>>>"""

# BEGIN
def my_map(function, source):
    for arg in source:  # noqa: WPS526
        yield function(arg)


def my_filter(condition, source):
    for arg in source:  # noqa: WPS526
        if condition(arg):
            yield arg


def replicate_each(number, source):
    for value in source:
        yield from (value for _ in range(number))
        # "yield from i", это сокращённая форма для
        #
        # for x in i:
        #     yield x
# END