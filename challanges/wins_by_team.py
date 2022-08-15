"""Предположим, что нам нужно анализировать результаты матчей "команда против команды" по некоторому виду спорта. Для простоты будем считать, что "ничья" в этом виде спорта не предусмотрена и каждый матч описывается парой (кортежем) строк, где первая именует победителя, а вторая проигравшего. И сами с собой команды пусть тоже не играют :)

Вам предстоит реализовать функцию wins_by_team(), которая должна принимать перечень (iterable) матчей в качестве единственного аргумента и возвращать словарь, ключами которого выступали бы имена команд, а значениями множества названий команд которых данная команда-ключ обыграла хотя бы раз.

>>> from solution import wins_by_team
>>> wins_by_team([])
{}
>>> wins_by_team([("A", "B")])
{'A': {'B'}}
>>> wins_by_team([("A", "B"), ("B", "A")])
{'A': {'B'}, 'B': {'A'}}
>>> wins_by_team(
...     [("A", "B"), ("B", "C"), ("A", "C")]
... ) == {'A': {'B', 'C'}, 'B': {'C'}}
...
True
>>>
Это задание можно выполнить в процедурном стиле с помощью defaultdict или dict.setdefault и изменяемых множеств, однако попробуйте описать декларативное решение с использованием comprehensions!"""

# BEGIN
def wins_by_team(games):
    winners = {team for team, _ in games}
    return {
        team: {looser for winner, looser in games if winner == team}
        for team in winners
    }
# END

# BEGIN (write your solution here)
def wins_by_team_2(data):
    result = dict()
    loser_set = set()
    for i in data:
        if i[0] not in result.keys():
            result[i[0]] = loser_set
            result[i[0]].add(i[1])
        loser_set = set()
        result[i[0]].add(i[1])

    return result
# END