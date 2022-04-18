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
P = [-4,-r]
Q = [4,-r]
A = [0,-r]
B = [r*np.sin(2*theta),-r*np.cos(2*theta)]
C = [r*np.sin(2*theta), r*np.cos(2*theta)]
D = [-r*np.sin(2*theta), r*np.cos(2*theta)]

def plot_point(P):
    plt.plot(P[0], P[1], marker = 'o')

def plot_line_segment(P1, P2):
    plt.plot([P1[0], P2[0]], [P1[1], P2[1]], 'b')

def mark_point(P, lab):
    plt.annotate(lab, xy=(P[0] - 0.3, P[1] + 0.3), textcoords='data')

#Plotting the points
plot_point(A)
plot_point(B)
plot_point(C)
plot_point(D)
plot_point(P)
plot_point(Q)
plt.plot([0], [0], 'o') # Center of the circle

#Plotting the line segments
plot_line_segment(P, Q) # Tangent to thr circle (PQ)
plot_line_segment(D, B) # Line segment DB
plot_line_segment(D, A) # Line segment DA
plot_line_segment(B, A) # Line segment BA
plot_line_segment(C, A) # Line segment AC
plot_line_segment(D, C) # Line segment DC
plot_line_segment(B, C) # Line segment BC

# Labelling the points, put a small offset so that the labels are not overlapping.
mark_point(A, 'A')
mark_point(B, 'B')
mark_point(C, 'C')
mark_point(D, 'D')
mark_point(P, 'P')
mark_point(Q, 'Q')

plt.xticks(np.arange(-4, 4))
plt.yticks(np.arange(-4, 4))

plt.show()
