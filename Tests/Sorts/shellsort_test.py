import Sorts.shellsort as s

def test_combsort_1():
    assert s.shellsort([4,2,1,7,9,5,5,3,8,6]) == [1,2,3,4,5,5,6,7,8,9]

def test_combsort_2():
    assert s.shellsort([1,2,3,4,5]) == [1,2,3,4,5]

def test_combsort_3():
    assert s.shellsort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]

def test_combsort_4():
    assert s.shellsort([]) == []