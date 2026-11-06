#Question : WAP to print a matrix containing group of similar elements by giving the input randomly in another matrix.

#Answer :
from collections import Counter
a = list(map(int, input("Enter elements: ").split()))
c = Counter(a)
m = [[k]*v for k, v in c.items()]
print("Original list: ", a)
print("Grouped matrix: ", m)

#Output:
'''Enter elements: 1 2 2 3 1 4
Original list:  [1, 2, 2, 3, 1, 4]
Grouped matrix:  [[1, 1], [2, 2], [3], [4]]'''