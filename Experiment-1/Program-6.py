#Question: WAP to convert distance in meters to Kilometers.

#Answer :
x = int(input("Enter the distance in meter: "))
y = int(x / 1000)
z = int(x % 1000)
print(y, "kilometer", z, "meter")

#Output:
'''Enter the distance in meter: 1500
1 kilometer 500 meter'''