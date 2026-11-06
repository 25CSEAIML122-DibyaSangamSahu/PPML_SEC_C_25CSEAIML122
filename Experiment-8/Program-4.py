#Question : WAP for Statistical operations and broadcasting on arrays.

#Answer :
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))
print(arr + 10)

#Output:
'''3.0
3.0
1.4142135623730951
2.0
[11 12 13 14 15]'''