#Question : WAP to enter two sets and perform all the set operations on it.

#Answer :
S1 = set(eval(input("Enter the 1st set : ")))
S2 = set(eval(input("Enter the 2nd set : ")))
print("Union operation is :", S1.union(S2))
print("Intersection operation is :", S1.intersection(S2))
print("The difference is :", S1.difference(S2))
print("The Symmetric-difference is :", S1.symmetric_difference(S2))

#Output:
'''Enter the 1st set : {1, 2, 3}
Enter the 2nd set : {3, 4, 5}
Union operation is : {1, 2, 3, 4, 5}
Intersection operation is : {3}
The difference is : {1, 2}
The Symmetric-difference is : {1, 2, 4, 5}'''