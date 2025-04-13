numbers = []
print("Enter number of elements you want in the list : ")
n = int(input())
print("Enter the elements of the list : ")
for i in range(0,n):
    number = float(input())
    numbers.append(number)
print("The inputted list is : ", numbers)
largest = max(numbers)
smallest = min(numbers)
average = sum(numbers)/len(numbers)
print("The largest number in the list is : ", largest)
print("The smallest number in the list is : ", smallest)
print("The average of the list is : ", average)

specific_number = float(input("Enter the number whose count needs to be found : " ))
c = numbers.count(specific_number)
print("The count of the number enterded is : ",c)
