def insertionsort(array):
    for i in range(len(array)):
        x = array[i]
        j = i
        while j > 0 and array[j-1] > x:
            array[j] = array[j-1]
            j = j-1
        array[j] = x
    return array

if __name__ == "__main__":
    print("result: ",insertionsort([4,2,1,7,9,5,5,3,8,6]))