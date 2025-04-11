def oddandeven():
    sum = 0
    for i in range(2,100):
        if (i%2 != 0):
            print(i)
    for i in range(2,100):
        if (i%2 == 0):
            sum = sum + i
    print(sum)

oddandeven()