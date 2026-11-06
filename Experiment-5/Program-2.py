#Question : WAP to create a dictionary and print the key which has the maximum unique value.

#Answer :
d = dict(eval(input("Enter the dictionary: ")))
S = []
s1 = []
for v in d.keys():
    S.append(v)
for val in d.values():
    s1.append(val)
mv = s1[0]
mk = S[0]
for i in range(1, len(S)):
    if s1[i] > mv:
        mv = s1[i]
        mk = S[i]
print("The key has maximum unique value is:", mk)

#Output:
'''Enter the dictionary: {'x': 10, 'y': 50, 'z': 30}
The key has maximum unique value is: y'''