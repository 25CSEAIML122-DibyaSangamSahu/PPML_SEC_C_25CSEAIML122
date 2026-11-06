#Question : WAP to draw the 3D-plot.

#Answer :
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [7, 1, 3, 3, 2])
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")
plt.show()

# Output:
'''Figure-5'''