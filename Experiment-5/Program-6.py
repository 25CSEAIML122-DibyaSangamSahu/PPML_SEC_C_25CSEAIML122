#Question : WAP to enter two different sets with sorting element combine both the sets remove any duplicates are present, print the new set.

#Answer :
S1 = set(eval(input("Enter the 1st set: ")))
S2 = set(eval(input("Enter the 2nd set: ")))
S3 = set()
S1.update(S2)
S3 = S1
print("After updation the new set is: ", S3)

#Output:
'''Enter the 1st set: {1, 2}
Enter the 2nd set: {2, 3}
After updation the new set is:  {1, 2, 3}'''