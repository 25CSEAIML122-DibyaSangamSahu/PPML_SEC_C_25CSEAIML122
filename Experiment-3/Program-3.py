#Question : WAP to check the leap year.

#Answer :
x = int(input("Enter a year: "))
if (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
    print(x, "is a leap year")
else:
    print(x, "is NOT a leap year")

#Output:
'''Enter a year: 2020
2020 is a leap year'''