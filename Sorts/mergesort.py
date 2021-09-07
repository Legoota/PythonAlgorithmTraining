def mergesort(array):
    if len(array) < 2:
        return array

    center = len(array)//2
    left, right = array[:center], array[center:]
    left = mergesort(left)
    right = mergesort(right)
    return mergelists(left, right)

def mergelists(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if(left[0] <= right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result