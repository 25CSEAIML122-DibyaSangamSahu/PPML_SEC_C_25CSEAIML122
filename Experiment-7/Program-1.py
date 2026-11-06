#Question : WAP to triple all numbers in a given list of integers. Use map().

#Answer :
a = list(eval(input("Enter a list: ")))
print(list(map(lambda x: x * 3, a)))

#Output:
'''Enter a list: [1, 2, 3, 4]
[3, 6, 9, 12]'''