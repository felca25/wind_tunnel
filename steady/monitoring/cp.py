import numpy as np
import re
from matplotlib import pyplot as plt

np.set_printoptions(precision=6)

tsr = 6.5
v_0 = 8.0

r = 0.11
# r = 0.055
# rho air at 25ºC
rho = 1.225
# rho = 998.2 # water at 25ºC
purge_before = -100
# purge_before = 4

if tsr == 3.5:
    t_init = "3.5"
elif tsr == 4.0:
    t_init = "4.0_TSR"
elif tsr == 5.0:
    t_init = 5.0
elif tsr == 4.5:
    t_init = 759
elif tsr == 1.0:
    # v_0=10
    # t_init = "1.01TSR"
    # t_init = 200
    t_init = 2
elif tsr == 1.5:
    t_init = 300
    v_0 = 12
elif tsr == 8.0:
    t_init = 1149
    # t_init = 2100
elif tsr == 7.0:
    t_init = 1472
elif tsr == 6.0:
    t_init = "6.0"
elif tsr == 6.5:
    t_init = 1760
elif tsr == 7.01:
    t_init = 1920
elif tsr == 7.5:
    t_init = 2000
elif tsr == 12.0:
    t_init = 2200



with open(f'steady/postProcessing/forcesIncompressible/{t_init}/forces.dat', 'r') as f:
    data = f.readlines()
    data = data[3:]
    data = [line.split(sep=' ') for line in data]
    numeric_values = [float(match.group())\
        for sublist in data for item in sublist\
            for match in re.finditer(r'-?\d+\.\d+e[+-]\d+', item)]
    result = []
    partial = []
    counter = 0
    line = 1
    for i in range(0,12*len(data)):
        partial.append(numeric_values[counter])
        counter += 1
        if counter == 12*line:
            result.append(partial)
            partial = []
            line += 1
        
    result = np.array(result)[1:]


A = np.pi * (r**2)

omega =  -tsr * v_0 / r # >> minus omega because omega > 1 indicates clockwise
energy = 0.5 * rho * A * (v_0**3)

forces_p = result[:,0:3]
forces_v = result[:,3:6]
forces = forces_p + forces_v

moment_p = result[:, 6:9]
moment_v = result[:,9:]
moment = moment_p + moment_v
# np.set_printoptions(precision=3)
print(f"Moment x: {moment[:,0]}")

# Omega = np.array([omega, 0, 0])
# moment_x = result[:, 6] + result[:, 9] 
thrust = forces[:,0]*v_0
ct = forces[:,0]*v_0/energy
power = moment[:,0] * omega
cp = (power/(energy))
eff = cp/0.593
cm = -moment[:,0]/(0.5*rho*(v_0**2)*A*r)

print(f'Kinetic energy: {energy}')
print('Power: ', power)
print(f"cp: {100*cp}")
print(f"Thrust: {thrust}")
print(f"ct: {ct*100}")
print(f"cm: {cm*100}")
print(f"Efficiency: {eff*100}")
t = np.linspace(0,len(cp), len(cp), dtype=int)
data_cp = np.array([t,cp, ct, cm])
data_cp = data_cp[:,purge_before:]

cp_avg = np.average(data_cp[1])
cp_prime = data_cp[1] - cp_avg
rms = np.std(data_cp[1])

ct_avg = np.average(data_cp[2])
ct_prime = data_cp[2] - ct_avg
ct_rms = np.std(data_cp[2])

cm_avg = np.average(data_cp[3])
cm_prime = data_cp[3] - cm_avg
cm_rms = np.std(data_cp[3])


np.set_printoptions(precision=3)
print("---------------------------------------------")
print(f"Measurements: {len(data_cp[1])}")
print(f"Angular velocity: {omega:.3f} rad/s")
print(f"Area: {A:.3f} m^2")
print("---------------------------------------------")
print(f"Average cp: {cp_avg*100:.2f}%")
print(f"Standard Deviation cp: {rms*100:.2f}%")
print(f"Average ct: {ct_avg*100:.2f}%")
print(f"Standard Deviation ct: {ct_rms*100:.2f}%")
print(f"Average cm: {cm_avg*100:.2f}")
print(f"Standard Deviation cm: {cm_rms*100:.2f}")
# print(f"Efficiency= {2* np.pi * np.mean(forces[:,0]*v_0)/ np.mean(moment[:,0]*omega):.2f}")
print(f"Efficiency= {(100*16*cp_avg)/27:.2f}")
print(f"RPM: {omega*60/(2*np.pi):.2f}")
#95% confidence interval
print(f"95% Confidence Interval: {257.6*rms/np.sqrt(len(data[0])):.2f}%") 
print("---------------------------------------------")

out = np.array([moment[:,0], power, cp])
header = f"TSR = {tsr:.1f}\n"\
    +f"Kinetic energy = {energy:.6e}\n"\
    +f"Angular velocity = {omega:.3f}\n"\
    +f"Area = {A:.6e}\n"\
    +f"Average = {cp_avg*100:.2f}%\n"\
    +f"Standard Deviation = {rms*100:.2f}%\n"\
    +f"95% Confidence Interval = {196*rms/np.sqrt(len(data[0])):.2f}%\n"\
        +f"moment_x[0] power[1] cp[2]"
        
np.savetxt(f"./steady/cp_{tsr:.1f}.dat", out.T, fmt="%.6e", header=header)

error = np.zeros(len(data_cp[1]))
for i in range(1, len(data_cp[1])):
    error[i] = (data_cp[1][i] - data_cp[1][i-1])/data_cp[1][i-1]
    error[i] *= 100
    if np.abs(error[i]) > 100:
        error[i] = 0
plt.rcParams['text.usetex'] = True
plt.style.use("seaborn-v0_8-muted")
plt.rcParams['font.family'] = 'Times New Roman'

fig = plt.figure()
ax = fig.add_subplot(211) 
ax.set_title("Power coefficient convergence $C_P$ at "
             +f"{tsr:.1f} TSR")
ax.plot(data_cp[0], 100*data_cp[1], marker='.', linestyle="-", c="#003EB3",
        linewidth=1.0)
ax.hlines(cp_avg*100, data_cp[0,0], data_cp[0,-1], 'k')
ax.hlines(rms*100+cp_avg*100, data_cp[0,0], data_cp[0,-1], 'k', linestyles="-.")
ax.hlines(-rms*100+cp_avg*100, data_cp[0,0], data_cp[0,-1], 'k', linestyles="-.")
ax.set(ylabel=r"$C_P[\%]$")

# x_ticks = np.linspace(min(data_cp[0]), max(data_cp[0]), 8, dtype=int)
# x_ticks  = ax.get_xticks()
# ax.set_xticks(x_ticks)
ax.grid(1, color='k', linestyle='--', alpha=0.2)
ax.set_xticklabels([])
legend = ax.legend([r"${C_P}_i$", 
            r"$\bar C_P = $"+f"{100*cp_avg:.3f}\%",
            r"$\sigma_P = \pm$"+f"{100*rms:.3f}\%"],loc='lower left')
legend.get_frame().set_alpha(0.95)
# ax.set_ylim(0, 60)
# ax.set_xlim(min(data_cp[0]), max(data_cp[0]))
ax2 = fig.add_subplot(212)
ax2.set_title(f"Torque coefficient convergence $C_M$ at {tsr:.1f} TSR")
ax2.set(ylabel=r"$C_M[\%]$", xlabel="Iterations $i$")
ax2.plot(data_cp[0], data_cp[3]*100, marker='.', linestyle="--",c="#003EB3")

ax2.hlines(cm_avg*100, data_cp[0,0], data_cp[0,-1], 'k')
ax2.hlines(cm_rms*100+cm_avg*100, data_cp[0,0], data_cp[0,-1], 'k', linestyles="-.")
ax2.hlines(-cm_rms*100+cm_avg*100, data_cp[0,0], data_cp[0,-1], 'k', linestyles="-.")
# ax2.legend([r"$\Delta c_p$"])
ax2.grid(1, color='k', linestyle='-', alpha=0.2)
legend = ax2.legend([r"${C_M}_i$", 
            r"$\bar C_M = $"+f"{100*cm_avg:.3f}\%",
            r"$\sigma_M = \pm$"+f"{100*cm_rms:.3f}\%"],loc='lower left')
legend.get_frame().set_alpha(0.95)
# ax2.set_xticks(x_ticks)

plt.savefig(f"steady/monitoring/cp_{tsr:.1f}.png", dpi=600, bbox_inches="tight")

BEM_diameter = 2.2      # //m
BEM_chord = 1.294e-1    # //m
BEM_velocity = 8        # //m/s
BEM_nu = 1.5e-5         # //m^2/s

Re = BEM_velocity * BEM_chord / BEM_nu

chord = BEM_chord/10
velocity = 8
# Re_new = 8.0 * chord / BEM_nu

print(f"Re: {Re:.3e}")
# print(f"Re_new: {Re_new:.3e}")

nu = velocity * chord / Re
print(f"nu: {nu:.3e}")