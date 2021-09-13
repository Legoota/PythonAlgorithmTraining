def shellsort(array):
    gap = len(array) // 2 # Gap is initialized to half the array's size

    while gap > 0:
        i = 0
        j = gap
        while j < len(array):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i] # Invert

            i += 1
            j += 1

            l = i
            while l-gap > -1:
                if array[l-gap] > array[l]:
                    array[l-gap], array[l] = array[l], array[l-gap] # Invert
                l -= 1

        gap //=2 # Reducing gap by half

    return array