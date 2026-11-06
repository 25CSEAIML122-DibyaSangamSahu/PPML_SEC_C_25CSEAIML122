#Question : WAP to input two dictionaries and print values by merging the two dictionaries.

#Answer :
dict1 = dict(eval(input("Enter 1st dictionary values: ")))
dict2 = dict(eval(input("Enter 2nd dictionary values: ")))
print(dict1)
print(dict2)
dict1.update(dict2)
print("After merging the list is: ")
print(dict1)

#Output:
'''Enter 1st dictionary values: {1: 'a', 2: 'b'}
Enter 2nd dictionary values: {3: 'c', 4: 'd'}
{1: 'a', 2: 'b'}
{3: 'c', 4: 'd'}
After merging the list is: 
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}'''