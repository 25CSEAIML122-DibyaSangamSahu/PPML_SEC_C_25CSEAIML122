#Question : WAP to enter a set and copy the content of the set into a new set one element at a time.

#Answer :
S = set(eval(input("Enter a set element: ")))
s1 = set()
for i in S:
    s1.add(i)
print("Updated set is :", s1)

#Output:
'''Enter a set element: {1, 2, 3}
Updated set is : {1, 2, 3}'''