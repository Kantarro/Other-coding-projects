import numpy as np

a = np.array([1,2,3], dtype='int16')
b = np.array([[[1.1,2.2,3.3],[3.9,20.1,2.9]],[[1.1,2.2,3.3],[3.9,20.1,2.9]]])
print(a)
print(b)
print("a's dimension is", a.ndim)
print("b's dimension is", b.ndim)
print(a.shape)
print(b.shape)
print(a.dtype)

c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# Get a specific element [row, column], index still starts at 0
print(c[1,3])
print(c[1,:]) # second row
print(c[:,2]) # third column (output as a row)
# [start index:end index:step size], end index exclusive!
print(c[0, 1:6:2])
print(c)
c[1,5] = 20
print(c)
c[:, 2] = 33 # same as [33,33]
print(c)

d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)
# get specific element (work outside in)
print(d[0,1,1]) # gets the 4
print(d[:,1,:]) # gets all the second rows
d[:,1,:] = [[9,9],[8,8]]
print(d)

zeros_matrix = np.zeros((2,3), dtype='int32') # all 0s matrix, tuple as argument for shape
print(zeros_matrix)
ones_matrix = np.ones((2,3), dtype='int32') # all 0s matrix, tuple as argument for shape
print(ones_matrix)
any_other = np.full((2,3), 77, dtype='float32') # all fill_value = some number matrix, tuple as argument for shape
print(any_other)

print(np.full_like(d, 2025)) # needs previously defined matrix for full_like
print(np.full(d.shape, 2001)) # needs previously defined matrix's shape for full

print(np.random.rand(4,2,3)) # random decimal numbers, NO tuple, just give numbers for dimensions
print(np.random.randint(-5,11, size=(2,3))) # random integer numbers, NO tuple, just give numbers for dimensions

print(np.identity(3,dtype='int32')) # identity [square] matrix

# repeat an array
arr1 = np.array([[1],[2],[3]])
r1 = np.repeat(arr1, 3, axis=1)
arr2 = np.array([[1,2,3]])
r2 = np.repeat(arr2, 2, axis=0)
print('r1 is', r1)
print('r2 is', r2)

practice_matrix = np.ones((5,5), dtype='int32')
practice_matrix[1:-1, 1:-1] = np.zeros((3,3), dtype='int32')
practice_matrix[2:-2, 2:-2] = np.full(1, 9, dtype='int32') # can use shape=1 or shape=(1,1)
print(practice_matrix)

# Be careful when copying arrays
A = np.array([1,2,3])
B = A
B[0] = 100
print('B is', B)
print('A is', A) # A and B both point to same object, so changing B will also change A here
A = np.array([1,2,3])
B = A.copy()
B[0] = 100
print('B is', B)
print('A is', A)

# operations done to each element
print('A+2 is', A+2)
print('A-2 is', A-2)
print('A*2 is', A*2)
print('A**2 is', A**2)
print('A+B is', A+B)
print('A*B is', A*B) # elementwise multiplication
print('sine of A is', np.sin(A))
print('cosine of A is', np.cos(A))

# linear algebra
a = np.array([[1,2,3],[3,4,9]]) # 2x3 matrix
b = np.array([[-1, 2],[-5,2],[9,2]]) # 3x2 matrix
product_matrix1 = np.matmul(a,b) # 2x2 matrix multiplication result, input a then b
product_matrix2 = a@b # another way without referencing np.
print(product_matrix1)
print(product_matrix2)
c = np.identity(3, 'int32')
print(np.linalg.det(c)) # find the determinant

# statistics
stats = np.array([[11,66,33],[44,55,77]])
print(np.min(stats, axis=0)) # gives min of first and second row
print(np.max(stats))
print(np.sum(stats))
print(np.sum(stats, axis=0))

# reorganizing arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before.shape)
after = before.reshape((8,1))
print(after)

# vertically stacking vectors
v1 = np.array([-43,2,9,5])
v2 = np.array([5,-6,9,2])
print(np.vstack((v1,v2))) # vertical stack
h1 = np.ones((2,4), dtype='int32')
h2 = np.zeros((2,2), dtype='int32')
print(np.hstack((h1,h2))) # horizontal stack