n = int(input("Enter a number : "))
print("The entered number is : ",n)

def primeornot(n):
    if(n<2):
        return False

    for i in range(2,int(n**0.5) + 1):
        if(n % i == 0):
            return False
    return True

answer = primeornot(n)
print (answer)