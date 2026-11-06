#Question : WAP to remove all duplicates from a given string.

#Answer :
a = input("Enter a string: ")
result = ""
for char in a:
    if char not in result:
        result = result + char
print(result)

#Output:
'''Enter a string: programming
progamin'''