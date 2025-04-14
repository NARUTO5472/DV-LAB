import numpy as np

# Generate two 3x3 matrices with random integers
random_matrix = np.random.randint(1, 100, size=(3, 3))
random_matrix2 = np.random.randint(1, 51, size=(3, 3))

# Print the generated matrices
print("Matrix 1:\n", random_matrix)
print("Matrix 2:\n", random_matrix2)

# Matrix addition
a = np.add(random_matrix, random_matrix2)
print("Addition of Matrices:\n", a)

# Matrix subtraction
s = np.subtract(random_matrix, random_matrix2)
print("Subtraction of Matrices:\n", s)

# Element-wise multiplication
m = np.multiply(random_matrix, random_matrix2)
print("Element-wise Multiplication of Matrices:\n", m)

# Transpose of matrices
t1 = np.transpose(random_matrix)
t2 = np.transpose(random_matrix2)
print("Transpose of Matrix 1:\n", t1)
print("Transpose of Matrix 2:\n", t2)

# Determinants of matrices
d1 = np.linalg.det(random_matrix)
d2 = np.linalg.det(random_matrix2)
print("Determinant of Matrix 1:", d1)
print("Determinant of Matrix 2:", d2)

# Inverse of matrices (only if determinant is not zero)
if d1 != 0:
    i1 = np.linalg.inv(random_matrix)
    print("Inverse of Matrix 1:\n", i1)
else:
    print("Matrix 1 has zero determinant, so it's not invertible.")

if d2 != 0:
    i2 = np.linalg.inv(random_matrix2)
    print("Inverse of Matrix 2:\n", i2)
else:
    print("Matrix 2 has zero determinant, so it's not invertible.")
