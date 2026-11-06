#Question : WAP to enter a percentage and display the gradation system.

#Answer :
x = float(input("Enter your percentage: "))
if x <= 100 and x >= 90:
    print("You got 'O' grade.")
elif x < 90 and x >= 80:
    print("You got 'E' grade.")
elif x < 80 and x >= 70:
    print("You got 'A' grade.")
elif x < 70 and x >= 60:
    print("You got 'B' grade.")
elif x < 60 and x >= 50:
    print("You got 'C' grade.")
elif x < 50 and x >= 40:
    print("You got 'D' grade.")
else:
    print("You got 'F' grade.")
    
#Output:
'''Enter your percentage: 85
You got 'E' grade.'''