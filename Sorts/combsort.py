import math

def combsort(array):
    length = len(array)
    shrink = 1.3
    gap = length
    out = list(array)
    sorted = False
    while not sorted:
        gap /= shrink
        newgap = int(gap)
        if newgap <= 1:
            sorted = True
            newgap = 1
        for i in range(length - newgap):
            sm = newgap + i
            if out[i] > out[sm]:
                out[i], out[sm] = out[sm], out[i]
                sorted = False
    return out

if __name__ == "__main__":
    print("result:",combsort([4,2,1,7,9,5,5,3,8,6]))