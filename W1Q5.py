s = input("Enter a string: ")
consonents = 0
vowels = 0
for i in s:
    if i in "aeiouAEIOU":
        vowels +=1
    elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consonents +=1
print("Vowels = ",vowels)
print("Consonents = ",consonents)
