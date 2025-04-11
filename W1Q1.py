a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print("The numbers inputted numbers are :",a,"and ",b)
func = input("Enter the operation you want to do : ")
answer = 0.0

if(func == '+'):
    answer = a+b
elif(func == '-'):
    answer = a-b
elif(func == '*'):
    answer = a*b
elif(func == '/'):
    answer = a/b
else:
    print("Invalid Input")
print(answer)
