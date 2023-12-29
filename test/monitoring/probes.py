import numpy as np
from matplotlib import pyplot as plt
import re

plt.style.use("seaborn-v0_8-muted")
plt.rcParams.update({"font.family": "Times New Roman",
                      "font.size": 12,
                      "text.usetex": True})

path = "test"
t_init = 1
i_min = 10

with open(f"test/postProcessing/probes/{t_init}/U") as f:
    data = f.readlines()
    data = data[3:]
    data = [line.split(' ')for line in data]
    # data = [item for sublist in data for item in sublist]
    for line in data:
        for i, item in enumerate(line):
            if item == '':
                line.pop(i)
            if '(' in item:
                line[i] = item[1:]
                velocity = [item]
            if '\n' in item:
                print(item)
                # line[i] = item[:-1]
            if ')' in item:
                line[i] = item[:-1]
                velocity.append(item[:-1])
print(data)

pressure_data = np.loadtxt(f"{path}/postProcessing/probes/{t_init}/p", 
                           unpack=1, skiprows=2)[:,i_min:]
x = pressure_data[0,:]

fig = plt.figure(figsize=[6,6])
ax = fig.add_subplot()
ax.set_title("Pressure Distribution on the Blade")
for i in range(1, len(pressure_data)):
    ax.plot(x, pressure_data[i,:], label=f"Probe {i}")
    # y = pressure_data[1,:]
# ax.plot(x, y, marker="o")
ax.set_xlabel("Iteration")
ax.set_ylabel("Pressure [Pa]")
ax.grid(1, linestyle="--", color='k', alpha=0.2)

plt.savefig(f"{path}/monitoring/pressure.png", dpi=600, bbox_inches="tight")