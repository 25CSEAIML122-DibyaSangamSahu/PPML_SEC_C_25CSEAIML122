#Question : WAP to print even length words in a string.

#Answer :
a = input("Enter a string: ")
y = ""
for c in a:
    if c == " ":
        if len(y) % 2 == 0:
            print(y)
        y = ""
    else:
        y = y + c
if len(y) % 2 == 0:
    print(y)
    
#Output:
'''Enter a string: Python is a great language
is
great'''