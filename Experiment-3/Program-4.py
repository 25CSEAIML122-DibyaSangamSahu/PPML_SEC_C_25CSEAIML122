#Question : WAP to check whether a string is symmetrical or palindrome.

#Answer :
x = input("Enter a String: ")
length = len(x)
if x == x[::-1]:
    print("The string is Palindrome")
else:
    print("The string is NOT Palindrome")
if length % 2 == 0:
    mid = length // 2
    if x[:mid] == x[mid:]:
        print("The string is symmetrical")
    else:
        print("The string is NOT symmetrical")
else:
    print("The string is NOT symmetrical")

#Output:
'''Enter a String: madam
The string is Palindrome
The string is NOT symmetrical'''