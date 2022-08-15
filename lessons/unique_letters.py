"""Вам необходимо реализовать функцию number_of_unique_letters(), которая должна подсчитывать количество уникальных букв в строке-аргументе без учёта регистра.

>>> from solution import number_of_unique_letters
>>> number_of_unique_letters("")
0
>>> number_of_unique_letters("abc")
3
>>> number_of_unique_letters("A-a-a-a-a-a!")
1
>>> number_of_unique_letters("\\(O_o)/")
1
>>> number_of_unique_letters("AaBbCcDd")
4
>>>"""

# BEGIN
def number_of_unique_letters(text):
    return len({char.lower() for char in text if char.isalpha()})
# END