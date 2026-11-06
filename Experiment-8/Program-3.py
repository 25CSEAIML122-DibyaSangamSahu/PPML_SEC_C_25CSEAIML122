#Question : WAP for Numpy array properties and functions.

#Answer :
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr.sum(1))
print(arr.max())
print(arr.min())
print(arr + 10)

#Output:
'''(2, 3)
2
6
int64
[ 6 15]
6
1
[11 12 13]
 [14 15 16]]'''