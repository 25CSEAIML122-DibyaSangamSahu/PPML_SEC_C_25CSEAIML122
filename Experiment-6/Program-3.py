#Question : WAP to print the transpose of a matrix of n order.

#Answer :
n = int(input("Enter order of matrix : "))
a = [list(map(int, input().split())) for i in range(n)]
print("Original Matrix: ")
for row in a:
    print(row)
print("Transpose: ")
for i in range(n):
    for j in range(n):
        print(a[j][i], end=" ")
    print()
    
#Output:
'''Enter order of matrix : 2
1 2
3 4
Original Matrix: 
[1, 2]
[3, 4]
Transpose: 
1 3 
2 4'''