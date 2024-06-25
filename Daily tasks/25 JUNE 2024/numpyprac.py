import numpy as np
#Shape
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c.shape)

#Size
a = np.array([1, 2, 3, 4, 5])
print(a.size)

#Datatype
a = np.array([1, 2, 3, 4, 5])
print(a.dtype) 

a = np.array([1, 2, 3], dtype=np.float32)
print(a)        
print(a.dtype)  

#Creating array from list
a = np.array([1, 2, 3, 4, 5])
print(a) 

#Convert input into array
d = (10, 20, 30)
b = np.asarray(d)
print(b) 

#Array with ones
b = np.ones((3, 4))
print(b)

#Array with zeros
b = np.zeros((2, 3))
print(b)

#Uninitialized array
b = np.empty((2, 3))
print(b)

#Arrange in sequence
a = np.arange(10)
print(a)

#Creating square matrix
a = np.eye(3)
print(a)

#Arithmetic Operations
#Addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)

#Subtraction
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = b - a
print(c) 

#Multiplication
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b
print(c) 

#Division
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = b / a
print(c)

#Square root
a = np.array([1, 4, 9])
b = np.sqrt(a)
print(b)

#Indexing
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0, 0])  
print(b[2, 1])

#Fancy indexing
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rows = np.array([0, 2])
cols = np.array([0, 2])
print(b[rows, cols])

#Boolean indexing
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[b > 5])

#Slicing
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0:2, 0:2])
print(b[:, 1])    
print(b[1:, :2])

a = np.array([1, 2, 3, 4, 5])
a[1:4] = 10
print(a)

#Concatenationg array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.stack((a, b))
print(c)
d=np.concatenate((a, b,), axis=None)
print(d)
e = np.array([[1, 2], [3, 4]])
f = np.array([[5, 6], [7, 8]])
g = np.concatenate((e, f), axis=0)
print(g)

#Splitting arrays
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])
left, right = np.hsplit(a, 2)
print("Horizontal split:")
print("Left sub-array:\n", left)
print("Right sub-array:\n", right)

#Append elements

a = np.array([1, 2, 3])
b = np.append(a, [4, 5])
print(b)
c = np.array([[1, 2], [3, 4]])
d = np.append(c, [[5, 6]], axis=0)
print(d)

#Insert elements
a = np.array([1, 2, 3, 4, 5])
b = np.insert(a, 2, [10, 20])
print(b) 
c = np.array([[1, 2], [3, 4]])
d = np.insert(c, 1, [10, 20], axis=1)
print(d)

#Deleting element

a = np.array([1, 2, 3, 4, 5])
b = np.delete(a, [0, 2])
print(b) 
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.delete(c, 1, axis=1)
print(d)

#Resize array
a = np.array([1, 2, 3, 4, 5])
b = np.resize(a, (3, 3))
print(b)