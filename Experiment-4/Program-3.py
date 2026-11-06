#Question : WAP to create an integer list of 20 elements increase the odd valued elements by 5.

#Answer :
S = []
n = int(input("Enter the no. of elements: "))
for i in range(n):
    val = int(input("Enter the element: "))
    S.append(val)
for i in range(n):
    if S[i] % 2 != 0:
        S[i] = S[i] + 5
print(S)

#Output:
'''Enter the no. of elements: 4
Enter the element: 1
Enter the element: 2
Enter the element: 3
Enter the element: 4
[6, 2, 8, 4]'''