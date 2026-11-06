#Question : WAP to enter an integer number and find out its binary, octal and hexadecimal equivalents.

#Answer :
x = int(input("Enter a number: "))
print(x)
print("Binary equivalent is: ", bin(x))
print("Octal equivalent is: ", oct(x))
print("Hexadecimal equivalent is: ", hex(x))

#Output:
'''Enter a number: 10
10
Binary equivalent is:  0b1010
Octal equivalent is:  0o12
Hexadecimal equivalent is:  0xa'''