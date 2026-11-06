#Question : WAP to enter a dictionary and remove the duplicate value inside the dictionary.

#Answer :
d = dict(eval(input("Enter the dictionary: ")))
temp = []
res = {}
for key, val in d.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
print(res)

#Output:
'''Enter the dictionary: {'a': 10, 'b': 20, 'c': 10}
{'a': 10, 'b': 20}'''