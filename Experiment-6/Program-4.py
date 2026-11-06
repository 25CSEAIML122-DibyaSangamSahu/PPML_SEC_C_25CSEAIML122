#Question: WAP to check if a value is present in the list or not, using lambda function.

#Answer:
a = list(map(int, input("Enter list elements: ").split()))
val = int(input("Enter element to search: "))
check = lambda x: x == val
if any(check(i) for i in a):
    print(val, "is present in the list")
else:
    print(val, "is not present in the list")
    
#Output:
'''Enter list elements: 10 20 30 40
Enter element to search: 30
30 is present in the list'''