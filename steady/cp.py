import numpy as np
import re
from matplotlib import pyplot as plt

tsr = 1.5
t_init = 522

v_0 = 8.0
r = 0.11
# rho air at 25ºC
rho = 1.225
purge_before = 2

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
        
    result = np.array(result)


A = np.pi * r**2
omega =  - tsr * v_0 / r # >> minus omega because of the MRF
energy = 0.5 * rho * A * v_0**3
moment_x = result[:, 6] + result[:, 9] 
print(result[:,6])
power = moment_x * omega
cp = power / energy

print(f'Kinetic energy: {energy}')
print('Power: ', power)
print(f"cp: {100*cp}")
t = np.linspace(t_init,t_init+len(cp), len(cp), dtype=int)
data_cp = np.array([t,cp])
data_cp = data_cp[:,purge_before:]

cp_avg = np.average(data_cp[1])
cp_prime = data_cp[1] - cp_avg
rms = np.std(data_cp[1])
print("---------------------------------------------")
print(f"Average: {cp_avg*100:.2f}%")
print(f"Standard Deviation: {rms*100:.2f}%")
print("---------------------------------------------")
# x = np.linspace(0, len(cp), len(cp), dtype=int)
plt.rcParams['text.usetex'] = True
plt.style.use("seaborn-v0_8-muted")
plt.rcParams['font.family'] = 'Times New Roman'

fig = plt.figure()
ax = fig.add_subplot()
ax.set_title("Power coefficient convergence $c_p$")
ax.scatter(data_cp[0], 100*data_cp[1])
ax.set(ylabel=r"Power Coefficient $c_p[\%]$", xlabel="Iteration")
ax.grid(1, color='k', linestyle='--', alpha=0.2)
ax.hlines(cp_avg*100, data_cp[0,0], data_cp[0,-1])
ax.hlines(rms*100+cp_avg*100, data_cp[0,0], data_cp[0,-1])
ax.hlines(-rms*100+cp_avg*100, data_cp[0,0], data_cp[0,-1])
plt.savefig(f"./cp_{tsr:.1f}.png")