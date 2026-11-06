#Question : WAP to create a list containing the power of said number in bases raised to the corresponding number in the index using python map.

#Answer :
n = list(eval(input("Enter power: ")))
y = list(eval(input("Enter bases: ")))
print(list(map(pow, y, n)))

#Output:
'''Enter power: [2, 3]
Enter bases: [2, 3]
[4, 27]'''