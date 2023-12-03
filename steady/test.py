import numpy as np
import re

with open('steady/postProcessing/forcesIncompressible/501/forces.dat', 'r') as f:
    data = f.readlines()
    data = data[3:]
    data = [line.split(sep=' ') for line in data]
    numeric_values = [float(match.group()) for sublist in data for item in sublist for match in re.finditer(r'-?\d+\.\d+e[+-]\d+', item)]
    result = []
    for j in range(len(data)):
        partial = []
        for i in range(0, 13):
            partial.append(numeric_values[i])
        result.append(partial)
    result = np.array(result)
    print(result)

v_0 = 8.0
r = 0.11
# rho air at 25ºC
rho 
rho = 1.225
A = np.pi * r**2
tsr = 2.0
omega = -tsr * v_0 / r
energy = 0.5 * rho * A * v_0**3
moment_x = result[:, 6] + result[:, 9] 
power = moment_x * omega
cp = power / energy

print(f'Kinetic energy: {energy}')
print('Power: ', power)
for cp in cp:
    print(f"Cp: {(100 * cp):.3f}%")
