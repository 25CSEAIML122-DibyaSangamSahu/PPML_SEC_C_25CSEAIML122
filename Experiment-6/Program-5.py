#Question : WAP to print Fibonacci series upto n terms using lambda function.

#Answer :
n = int(input("Enter number of terms: "))
fib = lambda a, b: (b, a + b)
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = fib(a, b)
    
#Output:
'''Enter number of terms: 6
0 1 1 2 3 5'''