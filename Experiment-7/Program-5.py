#Question : WAP to convert a given list of integer and a tuple of integer in a list of string using map().

#Answer :
x = list(eval(input("Enter list: ")))
tup = tuple(eval(input("Enter tuple: ")))
print(list(map(str, x)))
print(list(map(str, tup)))

#Output:
'''Enter list: [1, 2, 3]
Enter tuple: (4, 5, 6)
['1', '2', '3']
['4', '5', '6']'''