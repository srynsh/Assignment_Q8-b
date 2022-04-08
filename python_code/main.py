import matplotlib.pyplot as plt
import numpy as np

###
#### Suryaansh Jain
#### cs21btech11057
###

#### Q8 b)

figure, axes = plt.subplots()

axes.set_aspect(1)

a = np.linspace(0,2*np.pi,100000)

# r = 2, y' = x' = 0
y1 = 2*np.sin(a) # y = r sin(a) + y'
x1 = 2*np.cos(a) # x = r cos(a) + x'

plt.plot(x1, y1)

plt.plot([-4, 4], [-2, -2], 'b') # Tangent to thr circle (PQ)

#Plotting the points
plt.plot([0], [-2], 'o')
plt.plot([4], [-2], 'o')
plt.plot([-4], [-2], 'o')
plt.plot([np.sqrt(3)], [-1], 'o')
plt.plot([np.sqrt(3)], [1], 'o')
plt.plot([-1*np.sqrt(3)], [1], 'o')

#Plotting the line segments
plt.plot([-1*np.sqrt(3), np.sqrt(3)], [1, -1], 'b') # Line segment DB
plt.plot([-1*np.sqrt(3), 0], [1, -2], 'b') # Line segment DA
plt.plot([0, np.sqrt(3)], [-2, -1], 'b') # Line segment BA
plt.plot([0, np.sqrt(3)], [-2, 1], 'b') # Line segment AC
plt.plot([-1*np.sqrt(3), np.sqrt(3)], [1, 1], 'b') # Line segment DC
plt.plot([np.sqrt(3), np.sqrt(3)], [1, -1], 'b') # Line segment BC


# Labelling the points, put a small offset so that the labels are not overlapping.
plt.annotate('A', xy=(0, -2.3), textcoords='data')
plt.annotate('Q', xy=(4, -2.3), textcoords='data')
plt.annotate('P', xy=(-4, -2.3), textcoords='data')
plt.annotate('B', xy=(np.sqrt(3) + 0.3, -1), textcoords='data')
plt.annotate('D', xy=(-1*np.sqrt(3) - 0.3, 1), textcoords='data')
plt.annotate('C', xy=(np.sqrt(3) + 0.3, 1), textcoords='data')

plt.xticks(np.arange(-4, 4))
plt.yticks(np.arange(-4, 4))

plt.show()
