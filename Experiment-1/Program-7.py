#Question : WAP to enter time in minutes and print it in hour and minute format.

#Answer :
x = int(input("Enter the time: "))
h = int(x / 60)
m = int(x % 60)
print(h, "hour", m, "minute")

#Output:
'''Enter the time: 135
2 hour 15 minute'''