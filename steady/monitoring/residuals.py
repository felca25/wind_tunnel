import numpy as np
import os
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter

plt.rcParams['text.usetex'] = True
plt.style.use("seaborn-v0_8-muted")
plt.rcParams['font.family'] = 'Times New Roman'
# print(plt.style.available)

save_path = "."
t_init = 2

# residuals1 = np.loadtxt("steady/postProcessing/residuals/1/residuals.dat", 
#                        unpack=1, skiprows=3)[:,0:]

# residuals2 = np.loadtxt("steady/postProcessing/residuals/11/residuals.dat", 
#                        unpack=1, skiprows=3)[:,0:]

# residuals3 = np.loadtxt("steady/postProcessing/residuals/88/residuals.dat",
#                         unpack=1, skiprows=3)[:,0:]

residuals = np.loadtxt(f"steady/postProcessing/residuals/{t_init}/residuals.dat",
                        unpack=1, skiprows=3)[:,:]

# residuals = np.concatenate((residuals1, residuals2), axis=1)
# residuals = np.concatenate((residuals, residuals3)[::-1], axis=1)
# residuals = np.concatenate((residuals, residuals4), axis=1)

print(len(residuals[0]))
x = residuals[0]
x = np.linspace(x[0], x[-1], len(x), dtype=int)

fig = plt.figure(figsize=[6,4])
ax = fig.add_subplot()
ax.set_yscale('log')
ax.set_xlabel("Run Time [s]")
# ax.set_xlim(x[0], x[-1])
ax.set_ylabel(r"Residuals $\vec{U}/p/k$")
ax.set_xticks(np.linspace(x[0], x[-1], 10, dtype=int))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.d'))
ax.grid(1)

ax.set_title("Residual Monitoring for MRF Steady State Simulation")
ax.plot(x, residuals[1], label=r"$R(U_x)=$"+ f" {residuals[1][-1]:.2e}")
ax.plot(x, residuals[2], label=r"$R(U_y)=$"+f" {residuals[2][-1]:.2e}")
ax.plot(x, residuals[3], label=r"$R(U_z)=$"+f" {residuals[3][-1]:.2e}")
ax.plot(x, residuals[4], label=r"$R(p)=$"+f" {residuals[4][-1]:.2e}")
ax.plot(x, residuals[5], label=r"$R(k)=$"+f" {residuals[5][-1]:.2e}")
ax.set_yscale('log')
ax.set_ylabel(r"Residuals $\omega$")
# ax.plot(x, residuals[6], label=r"$R(\omega)=$"+f" {residuals[6][-1]:.2e}")
ax.grid(1, linestyle="--", color='k', alpha=0.2)

plt.legend(loc="lower left")
plt.tight_layout()
plt.savefig("steady/monitoring/residuals.png", dpi=600)
# plt.savefig(save_path+"/residual.png",
#             dpi=600)
# os.system("clear")
print("Plotted residuals.png successfully!")