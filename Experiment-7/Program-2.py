#Question : WAP to add three given list using python map and lambda.

#Answer :
x = list(eval(input("Enter 1st list: ")))
y = list(eval(input("Enter 2nd list: ")))
z = list(eval(input("Enter 3rd list: ")))
print(list(map(lambda a, b, c: a + b + c, x, y, z)))

#Output:
'''Enter 1st list: [1, 2]
Enter 2nd list: [3, 4]
Enter 3rd list: [5, 6]
[9, 12]'''