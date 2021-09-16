import Sorts.quicksort as q

def test_mergesort_1():
    assert q.quicksort([4,2,1,7,9,5,5,3,8,6]) == [1,2,3,4,5,5,6,7,8,9]

def test_mergesort_2():
    assert q.quicksort([1,2,3,4,5]) == [1,2,3,4,5]

def test_mergesort_3():
    assert q.quicksort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]

def test_mergesort_4():
    assert q.quicksort([]) == []