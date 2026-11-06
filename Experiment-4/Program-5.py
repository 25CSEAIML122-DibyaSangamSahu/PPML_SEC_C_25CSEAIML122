#Question : WAP to create a function that takes list as argument and returns the even values of the list. Print the new list with even values.

#Answer :
def even_elem(n):
    S = []
    for i in n:
        if i % 2 == 0:
            S.append(i)
    return S
a_input = input("Enter the list elements: ")
lst = [int(i) for i in a_input.split(",")]
print(even_elem(lst))

#Output:
'''Enter the list elements: 1, 2, 3, 4, 5, 6
[2, 4, 6]'''