import Strings.levenshtein as l

def test_levenshtein_1():
    assert l.levenshtein("sitting", "kitten") == 3

def test_levenshtein_2():
    assert l.levenshtein("sitting", "kitten") == l.levenshtein("kitten", "sitting")

def test_levenshtein_3():
    assert l.levenshtein("Sunday", "Saturday") == 3

def test_levenshtein_4():
    assert l.levenshtein("Hello world!", "Holy grail!") == 8