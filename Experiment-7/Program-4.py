#Question : WAP to convert all the characters into uppercase and lower case and eliminate duplicate letters from a given sequence Use map() function.

#Answer :
a = list(input("Enter characters: "))
print(set(map(lambda x: x.lower() if x.isupper() else x.upper(), a)))

#Output:
'''Enter characters: ['a', 'B', 'c', 'A']
{'a', 'b', 'C', 'c', 'A'}'''