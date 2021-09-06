import Sorts.insertionsort as i

def test_insertionsort_1():
    assert i.insertionsort([4,2,1,7,9,5,5,3,8,6]) == [1,2,3,4,5,5,6,7,8,9]

def test_insertionsort_2():
    assert i.insertionsort([1,2,3,4,5]) == [1,2,3,4,5]

def test_insertionsort_3():
    assert i.insertionsort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]

def test_insertionsort_4():
    assert i.insertionsort([]) == []