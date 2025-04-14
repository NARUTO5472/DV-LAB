import numpy as np

random_array = np.random.randint(1, 51, size=(3, 4))

print(random_array)
m = np.mean(random_array)
M = np.median(random_array)
sd = np.std(random_array)
print("Mean: ",m)
print("Median: " ,M)
print("Standard deviation: ",sd)

S = np.sum(random_array)
s = np.sum(random_array,axis = 0)
print(S)
print(s)

reshape = random_array.reshape(2,6)
print(reshape)
