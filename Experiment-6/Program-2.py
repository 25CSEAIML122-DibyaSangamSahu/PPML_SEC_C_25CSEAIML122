#Question : WAP to print a matrix along with a summation of row elements and column elements after entering a 3*3 matrix.

#Answer :
a = [list(map(int, input().split())) for i in range(3)]
for i in range(3):
    print(a[i], sum(a[i]))
print("-" * 20)
for j in range(3):
    print(sum(a[i][j] for i in range(3)), end=" ")
print()

#Output:
'''1 2 3
4 5 6
7 8 9
[1, 2, 3] 6
[4, 5, 6] 15
[7, 8, 9] 24
--------------------+
12 15 18'''