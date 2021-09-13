import Sorts.cocktailshakersort as c

def test_bubblesort_1():
    assert c.cocktailshakersort([4,2,1,7,9,5,5,3,8,6]) == [1,2,3,4,5,5,6,7,8,9]

def test_bubblesort_2():
    assert c.cocktailshakersort([1,2,3,4,5]) == [1,2,3,4,5]

def test_bubblesort_3():
    assert c.cocktailshakersort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]

def test_bubblesort_4():
    assert c.cocktailshakersort([]) == []