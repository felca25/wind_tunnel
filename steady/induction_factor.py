import numpy as np
from matplotlib import pyplot as plt
# from matplotlib import tri
import time
import matplotlib.tri as mtri

start_time = time.time()

# Load data
data = np.loadtxt('steady/induction_factor.txt', 
                  skiprows=1, unpack=True, delimiter=',')
coords = data[:3]
ux = data[3]

u0 = 8.0
a = 1 - (ux/u0)
for i in range(len(a)):
    lim = 0.5
    if a[i] > lim : a[i] = 0.8
    
# Create triangulation
triang = mtri.Triangulation(coords[2], coords[1])
# Plot contours
plt.rcParams.update({'font.size': 12, 'font.family': 'Times New Roman'})
plt.rcParams['text.usetex'] = True
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax.set_title(r'Contour plot of axial induction factor $a$')
ax.set(xlabel=r'$z$ [m]', ylabel=r'$y$ [m]', xlim=[-.15, .15], ylim=[-.15, .15])
contour = ax.tricontourf(triang, a, 25, cmap=plt.cm.jet)
# contour_labels = ax.tricontour(triang, a, 10, colors='w', linewidths=0.5)
# ax.clabel(contour_labels, inline=True, fontsize=8, fmt='%.2f')

plt.colorbar(contour, label=r'$a$', ax=ax, 
             ticks=np.linspace(a.min(), a.max(), num=10))
plt.tight_layout()

# save the plot
plt.savefig('steady/induction_factor.png')

# Calculate and print the execution time
print("Execution time: %s seconds" % (time.time() - start_time))



