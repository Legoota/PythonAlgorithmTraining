def quicksort(array):
    return quicksort_main(array,0,len(array)-1)

def quicksort_main(array, start, end):
    if start < end and (start >= 0 and end >=0):
        p = partition(array, start, end)

        quicksort_main(array, start, p-1)
        quicksort_main(array, p+1, end)

    return array

def partition(array, start, end):
    pivot_index = start 
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end