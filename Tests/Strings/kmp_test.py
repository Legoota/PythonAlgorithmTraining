import Strings.kmp as k

def test_kmp_1():
    assert k.kmp("ABC","ABDACABAB AABACAABC") == [16]

def test_kmp_2():
    assert k.kmp("AAA","AABBBCCCABAABCCAAB") == []

def test_kmp_3():
    assert k.kmp("Hello", "Salut Guten Tag Hello Hola") == [16]

def test_kmp_4():
    assert k.kmp("123456", "234561 12346 213645 123456 342516") == [20]