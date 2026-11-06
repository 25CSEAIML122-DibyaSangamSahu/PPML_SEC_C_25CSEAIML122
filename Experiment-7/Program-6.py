#Question : WAP to find the ratio of positive numbers, negative number and zeros in an array of integers using map().

#Answer :
x = list(eval(input("Enter integers: ")))
n = len(x)
print([
    round(sum(1 for i in x if i > 0) / n, 2),
    round(sum(1 for i in x if i < 0) / n, 2),
    round(sum(1 for i in x if i == 0) / n, 2)
])

#Output:
'''Enter integers: [1, -2, 0, 4]
[0.5, 0.25, 0.25]'''