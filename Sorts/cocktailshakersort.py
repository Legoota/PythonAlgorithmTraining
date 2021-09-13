def cocktailshakersort(array):
    swapped = True
    start = 0
    end = len(array)-1
    while swapped:
        swapped = False
        # Same as bubble sort
        for i in range (start, end):
            if (array[i] > array[i+1]) :
                array[i], array[i+1]= array[i+1], array[i]
                swapped=True

        if (swapped==False): # If nothing changes then the array is sorted
            break

        swapped = False
        end = end-1
  
        for i in range(end-1, start-1,-1):
            if (array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
  
        start = start+1
        
    return array

if __name__ == "__main__":
    print("result:",cocktailshakersort([4,2,1,7,9,5,5,3,8,6]))