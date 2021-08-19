def fizzbuzz(n):
    p = "" # not needed in general case, here just for testing purposes
    for i in range(1,n+1):
        p = ""
        if i % 3 == 0: p += "Fizz"
        if i % 5 == 0: p += "Buzz"
        print(p if len(p) > 0 else i)

    # last printed value returned for testing purposes
    return p