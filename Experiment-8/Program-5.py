#Question: WAP for saving and Loading arrays.

#Answer:
import numpy as np
arr = np.array([1, 2, 3, 4])
np.save('my_array', arr)
x = np.load('my_array.npy')
print(x)

#Output:
'''[1 2 3 4]'''