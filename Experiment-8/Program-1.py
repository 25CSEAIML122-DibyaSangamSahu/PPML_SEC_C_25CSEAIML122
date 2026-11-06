#Question : WAP for array Object, Indexing, and slicing in Numpy.

#Answer :
import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60]])
print(arr)
print(arr[0, 1])
print(arr[1, :])
print(arr[:, 2])

#Output:
'''[[10 20 30]
 [40 50 60]]
20
[40 50 60]
[30 60]'''