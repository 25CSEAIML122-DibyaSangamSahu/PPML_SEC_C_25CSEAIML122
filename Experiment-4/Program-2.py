#Question : WAP to create two lists first list containing integers and second list containing 5 strings. Print both the lists one element from each list combined at a time.

#Answer :
list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D", "E"]
S = []
for i in range(len(list1)):
    S.append(str(list1[i]))
    S.append(list2[i])
print(S)

#Output:
'''['1', 'A', '2', 'B', '3', 'C', '4', 'D', '5', 'E']'''