def bubblesort(array):
    for i in range(len(array),0,-1):
        sorted = True # Optimization in case the input array is already sorted => O(n)=1
        for j in range(i-1):
            if(array[j+1] < array[j]):
                array[j+1], array[j] = array[j], array[j+1]
                sorted = False
        if(sorted): return array
    return array