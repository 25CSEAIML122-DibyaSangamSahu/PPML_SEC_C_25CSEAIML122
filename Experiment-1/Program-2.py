#Question : WAP to enter three sides of a triangle. Find out the area of the triangle.

# Answer : 
import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c : "))
s = float((a + b + c) / 2)
Z = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of triangle is :", Z)

#Output:
'''Enter the value of a: 3
Enter the value of b: 4
Enter the value of c : 5
Area of triangle is : 6.0'''