#Question : WAP to create a function that prints the first 15 terms of the fibonacci series without using recursion.

#Answer :
def fibonacci(n):
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
n = int(input("Enter the number of terms you want to print: "))
print("The Fibonacci series of first", n, "terms are: ")
fibonacci(n)

#Output:
'''Enter the number of terms you want to print: 15
The Fibonacci series of first 15 terms are: 
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377'''