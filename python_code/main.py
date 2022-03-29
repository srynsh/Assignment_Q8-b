import matplotlib.pyplot as plt
import numpy as np

###
#### Suryaansh Jain
#### cs21btech11057
###

#### Q8 b)

figure, axes = plt.subplots()
Drawing_uncolored_circle = plt.Circle((0, 0), 2, fill=False)

axes.set_aspect(1)
axes.add_artist(Drawing_uncolored_circle)

plt.plot([-4, 4], [-2, -2], 'b')
plt.plot([0], [-2], 'o')
plt.plot([4], [-2], 'o')
plt.plot([-4], [-2], 'o')
plt.plot([np.sqrt(3)], [-1], 'o')
plt.plot([np.sqrt(3)], [1], 'o')
plt.plot([-1*np.sqrt(3)], [1], 'o')
plt.plot([-1*np.sqrt(3), np.sqrt(3)], [1, -1], 'b')
plt.plot([-1*np.sqrt(3), 0], [1, -2], 'b')
plt.plot([0, np.sqrt(3)], [-2, -1], 'b')

plt.plot([0, np.sqrt(3)], [-2, 1], 'b')
plt.plot([-1*np.sqrt(3), np.sqrt(3)], [1, 1], 'b')
plt.plot([np.sqrt(3), np.sqrt(3)], [1, -1], 'b')

plt.annotate('A', xy=(0, -2.3), textcoords='data')
plt.annotate('Q', xy=(4, -2.3), textcoords='data')
plt.annotate('P', xy=(-4, -2.3), textcoords='data')
plt.annotate('B', xy=(np.sqrt(3) + 0.3, -1), textcoords='data')
plt.annotate('D', xy=(-1*np.sqrt(3) - 0.3, 1), textcoords='data')
plt.annotate('C', xy=(np.sqrt(3) + 0.3, 1), textcoords='data')

plt.xticks(np.arange(-4, 4))
plt.yticks(np.arange(-4, 4))

plt.show()
