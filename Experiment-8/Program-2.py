#Question : WAP for data types and structures in NumPy.

#Answer :
import numpy as np
arr = np.array([1, 2, 3], dtype='int32')
print(arr.dtype)
arr = arr.astype('float64')
print(arr, arr.dtype)

#Output:
'''int32
[1. 2. 3.] float64'''