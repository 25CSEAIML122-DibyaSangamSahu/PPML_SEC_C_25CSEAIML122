#Question : WAP to enter a 5 digit number and print the digits present at odd locations.

#Answer :
a = []
n = int(input("Enter a 5 digit number: "))
print(f"The given number is {n}")
while n > 0:
    rem = n % 10
    a.append(rem)
    n = n // 10
a.reverse()
for i in range(0, len(a), 2):
    print(a[i], end=" ")

#Output:
'''Enter a 5 digit number: 12345
The given number is 12345
1 3 5'''