import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams.update({'font.size': 10,
                     'font.family': 'Times New Roman', 
                     'text.usetex': True})

d = 0.22
N = 20

Nx = 6 * N
Ny = 2 * N
Nz = Ny

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x_ticks = [-2*d, 0, 3]
y_ticks = [d, 0, -d]
z_ticks = [-d, 0, d]

x_tickslabels = [r'$-2d$', r'$0$', r'$3$']
y_tickslabels = [r'$d$', r'$0$', r'$-d$']
z_tickslabels = [r'$-d$', r'$0$', r'$d$']

x = np.linspace(-2*d, 6*d, Nx)
y = np.linspace(-d, d, Ny)
z = np.linspace(-d, d, Nz)
X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, np.ones((Ny,Nx))*(-d), color='white', alpha=0.5)

ax.set(xticks=x_ticks, yticks=y_ticks, zticks=z_ticks)
ax.set(xlabel='x', ylabel='y', zlabel='z')
ax.set(xticklabels=x_tickslabels, yticklabels=y_tickslabels,
       zticklabels=z_tickslabels)

ax.set(xlim=[-2*d, 3], ylim=[-d, d], zlim=[-d, d])

ax.view_init(elev=30, azim=180+25, )
ax.set_aspect('equal')
ax.grid(1, which='major', color='black', linestyle='--', alpha=0.5)
fig.tight_layout()

plt.savefig('backgroundMesh.png', dpi=600, bbox_inches='tight')