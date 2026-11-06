#Question : WAP to print the intersection of 2 arrays using Lambda function.

#Answer :
a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))
intersection = list(filter(lambda x: x in b, a))
print("Intersection:", intersection)

#Output:
'''Enter first array: 1 2 3 4
Enter second array: 3 4 5 6
Intersection: [3, 4]'''