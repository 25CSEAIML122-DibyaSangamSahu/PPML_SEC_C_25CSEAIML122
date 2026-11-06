#Question : WAP to draw Histograms and box plots.

#Answer :
import matplotlib.pyplot as plt
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]
plt.hist(data, bins=5)
plt.show()
plt.boxplot(data)
plt.show()

# Output:
'''Figure-3.1'''
'''Figure-3.2'''