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

# The inputs
r = 2
theta = (np.pi)/6

# The Points
Xp = -4
Yp = -2
Xq = 4
Yq = -2
Xa = 0
Ya = -r
Xb = r*np.sin(2*theta)
Yb = -r*np.cos(2*theta)
Xc = r*np.sin(2*theta)
Yc = r*np.cos(2*theta)
Xd = -r*np.sin(2*theta)
Yd = r*np.cos(2*theta)

#Plotting the points
plt.plot(Xa, Ya, 'o')
plt.plot(Xb, Yb, 'o')
plt.plot(Xc, Yc, 'o')
plt.plot(Xd, Yd, 'o')
plt.plot(Xp, Yp, 'o')
plt.plot(Xq, Yq, 'o')
plt.plot([0], [0], 'o') # Center of the circle

#Plotting the line segments
plt.plot([Xp, Xq], [Yp, Yq], 'b') # Tangent to thr circle (PQ)
plt.plot([Xd, Xb], [Yd, Yb], 'b') # Line segment DB
plt.plot([Xd, Xa], [Yd, Ya], 'b') # Line segment DA
plt.plot([Xb, Xa], [Yb, Ya], 'b') # Line segment BA
plt.plot([Xa, Xc], [Ya, Yc], 'b') # Line segment AC
plt.plot([Xd, Xc], [Yd, Yc], 'b') # Line segment DC
plt.plot([Xb, Xc], [Yb, Yc], 'b') # Line segment BC


# Labelling the points, put a small offset so that the labels are not overlapping.
plt.annotate('A', xy=(0, Ya-0.3), textcoords='data')
plt.annotate('Q', xy=(Xq, Yq-0.3), textcoords='data')
plt.annotate('P', xy=(Xp, Yp-0.3), textcoords='data')
plt.annotate('B', xy=(Xb + 0.3, Yb), textcoords='data')
plt.annotate('D', xy=(Xd - 0.3, Yd), textcoords='data')
plt.annotate('C', xy=(Xc + 0.3, Yc), textcoords='data')
plt.annotate('O', xy=(0.1, 0), textcoords='data')

plt.xticks(np.arange(-4, 4))
plt.yticks(np.arange(-4, 4))

plt.show()
