#Array Operations and Broadcasting

#1. Given a 3D array a with shape (2, 3, 4) and a 2D array b with shape (3, 4), perform element-wise multiplication between a and b using broadcasting.
import numpy as np
a = np.array([[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]], [[13, 14, 15, 16],[17, 18, 19, 20],[21, 22, 23, 24]]])
b = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
result = a * b
print("1.")
print(a.shape)
print(b.shape)
print("3D array:\n", a)
print("2D array:\n", b)
print("Multiplication:\n", result)

#Indexing and Slicing

#2. Given a 3D array g with shape (4, 3, 2), extract every other element along the first and second dimensions, but keep all elements along the third dimension.
g = np.array([[[1, 2],[3, 4],[5, 6]],[[7, 8],[9, 10],[11, 12]],[[13, 14],[15, 16],[17, 18]],[[19, 20],[21, 22],[23, 24]]])
result = g[::2, ::2, :]
print("2.")
print(g.shape)
print("Original array g:\n", g)
print("\nExtracted array:\n", result)

#Array manipulation

#3. Given a 2D array n with shape (4, 6), reshape it into a 3D array with shape (2, 2, 6) and then flatten it back to a 2D array with shape (4, 6).
n = np.array([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12],[13, 14, 15, 16, 17, 18],[19, 20, 21, 22, 23, 24]])
n_3d = n.reshape((2, 2, 6))
n_flattened = n_3d.reshape((4, 6))
print("Original 2D array n:\n", n)
print("\nReshaped 3D array (2, 2, 6):\n", n_3d)
print("\nFlattened back to 2D array (4, 6):\n", n_flattened)



