#Question : WAP to enter a number and check whether it is a Palindrome number or not.

#Answer :
x = int(input("Enter a number: "))
temp = x
rev = 0
while x > 0:
    y = x % 10
    rev = rev * 10 + y
    x = x // 10
if temp == rev:
    print("It is a Palindrome Number")
else:
    print("It is NOT a Palindrome Number")
    
#Output:
'''Enter a number: 121
It is a Palindrome Number'''