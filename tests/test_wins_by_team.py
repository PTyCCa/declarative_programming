from challanges.wins_by_team import wins_by_team


def test_wins_by_team():
    assert isinstance(wins_by_team([]), dict), "Function should return a dict"
    assert wins_by_team([]) == {}
    assert wins_by_team([("Griffindor", "Slytherin")]) == {
        "Griffindor": {"Slytherin"},
    }
    assert wins_by_team([
        ("X", "Y"),
        ("Y", "Z"),
        ("X", "Z"),
    ]) == {'X': {'Y', 'Z'}, 'Y': {'Z'}}
    assert wins_by_team([
        ('A', 'T'),
        ('C', 'G'),
        ('G', 'C'),
        ('C', 'G'),
        ('T', 'A'),
        ('A', 'T'),
        ('T', 'A'),
        ('T', 'A'),
        ('G', 'C'),
        ('G', 'C'),
    ]) == {'A': {'T'}, 'C': {'G'}, 'G': {'C'}, 'T': {'A'}}