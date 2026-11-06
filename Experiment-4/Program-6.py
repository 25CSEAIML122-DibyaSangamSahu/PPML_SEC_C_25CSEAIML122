#Question : WAP to calculate factorial of a number using recursion.

#Answer :
def factorial(n):
    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result
n = int(input("Enter the number: "))
if n < 0:
    print("It is a Negative number")
else:
    print("Factorial of", n, "is:", factorial(n))
    
#Output:
'''Enter the number: 4
Factorial of 4 is: 24'''