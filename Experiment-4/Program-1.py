#Question : WAP to print the second largest and second smallest element in a list of 10 integers without using sort function.

#Answer :
ans = []
n = int(input("Enter the no. of elements: "))
for i in range(n):
    m = int(input("Enter the element: "))
    ans.append(m)
for j in range(len(ans) - 1):
    for k in range(len(ans) - j - 1):
        if ans[k] > ans[k + 1]:
            ans[k], ans[k + 1] = ans[k + 1], ans[k]
print("The sorted array is: ")
print(ans)
second_largest = ans[-2]
second_smallest = ans[1]
print("Second largest element is:", second_largest)
print("Second smallest element is:", second_smallest)

#Output:
'''Enter the no. of elements: 5
Enter the element: 10
Enter the element: 40
Enter the element: 20
Enter the element: 50
Enter the element: 30
The sorted array is: 
[10, 20, 30, 40, 50]
Second largest element is: 40
Second smallest element is: 20'''