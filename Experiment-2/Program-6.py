#Question : WAP to enter a 3 digit number and print all the prime factors of the number.

#Answer :
x = int(input("Enter a 3 digit number: "))
c = 2
while (x > 1):
    if (x % c == 0):
        print(c, end=" ")
        x = x / c
    else:
        c = c + 1
        
#Output:
'''Enter a 3 digit number: 120
2 2 2 3 5'''