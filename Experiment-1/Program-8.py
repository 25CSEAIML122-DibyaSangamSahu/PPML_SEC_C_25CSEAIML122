#Question : WAP to enter two numbers and swap them using bitwise operators.

#Answer :
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print("Before swapping the value of a=", a, "and b=", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping the value of a=", a, "and b=", b)

#Output:
'''Enter the value of a : 5
Enter the value of b : 9
Before swapping the value of a= 5 and b= 9
After swapping the value of a= 9 and b= 5'''