import numpy as np

# Question 1
arr = np.array([1, 2, 3, 4, 5])

print("Array:")
print(arr)
print()

# Question 2
print("Mean:")
print(arr.mean())
print()

# Question 3
print("Max:")
print(arr.max())
print()

# Question 4
print("Min:")
print(arr.min())
print()

# Question 5
print("Sum:")
print(arr.sum())
print()

# Question 6
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matrix:")
print(matrix)
print()

print("Shape:")
print(matrix.shape)
print()

print("Zeros:")
print(np.zeros((3, 3)))
print()

print("Ones:")
print(np.ones((3, 3)))
print()

print("Reshape:")
print(np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3))