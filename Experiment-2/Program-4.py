#Question : WAP to enter a number and check whether the number is a perfect number or not.

#Answer :
x = int(input("Enter a number: "))
S = 0
for i in range(1, x):
    if (x % i == 0):
        S = S + i
if (S == x):
    print("It is a Perfect Number")
else:
    print("It is NOT a Perfect Number")
    
#Output:
'''Enter a number: 6
It is a Perfect Number'''