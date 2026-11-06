#Question : WAP to enter the coefficients of a quadratic equation and find out the roots of the equivalent equation.

#Answer :
import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c : "))
d = b * b - 4 * a * c
if d > 0:
    d = math.sqrt(d)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    print("The roots are:", x1, "and", x2)
elif d == 0:
    print("Both roots are equal:")
    x = -b / (2 * a)
    print("Root is:", x)
else:
    print("The roots are imaginary (Complex).")
    
#Output:
'''Enter the value of a: 1
Enter the value of b: -5
Enter the value of c : 6
The roots are: 3.0 and 2.0'''