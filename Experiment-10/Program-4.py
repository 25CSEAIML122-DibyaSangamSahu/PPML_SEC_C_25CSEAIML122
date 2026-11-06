#Question : WAP to draw Pie charts and contour plots.

#Answer :
import matplotlib.pyplot as plt
import numpy as np
plt.pie([15, 30, 45, 10], labels=['A', 'B', 'C', 'D'])
plt.show()
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contour(X, Y, Z)
plt.colorbar()
plt.show()

# Output:
'''Figure-4.1'''
'''Figure-4.2'''