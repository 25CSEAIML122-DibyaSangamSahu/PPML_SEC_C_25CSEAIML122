#Question : WAP to draw the scatter and bar plot.

#Answer :
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [4, 7, 6, 8, 7]
plt.scatter(x, y)
plt.show()
plt.bar(['A', 'B', 'C', 'D'], [3, 2, 8, 5])
plt.show()

# Output:
'''Figure-2.1'''
'''Figure-2.2'''