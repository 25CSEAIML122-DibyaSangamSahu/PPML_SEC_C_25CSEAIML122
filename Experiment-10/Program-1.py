#Question : WAP to plot a simple graph using matplotlib.

#Answer :
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, 'r--', label="Data")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Line Plot")
plt.legend()
plt.grid()
plt.show()


# Output:
'''Figure-1'''