import Strings.palindrome as p

def test_pal_1():
    assert p.palindrome('abcd dcba') == True

def test_pal_2():
    assert p.palindrome('Pull up if I pull up') == True

def test_pal_3():
    assert p.palindrome('Pull up if I pll up') == False

def test_pal_4():
    assert p.palindrome('12345431') == False