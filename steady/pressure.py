import numpy as np

data_type = "point"

data = np.loadtxt("steady/velocity.csv", delimiter=",", skiprows=1)
if data_type == "cell":
    velocity_vec = data[:,1:]
    
elif data_type == "point":
    coords = data[:,0:3]
    velocity_vec = data[:,3:]

else:
    raise ValueError("Invalid data type! Valid options are 'cell' and 'point'.")
# pressure = data[:,6]
# print(data[:,3:])

vel = []
for i in range(len(coords)):
    if coords[i, 1] >= -0.11 and coords[i, 1] <= 0.11:
        if coords[i, 2] >= -0.11 and coords[i, 2] <= 0.11:
            vel.append(velocity_vec[i,:])
            
vel = np.array(vel)

free_stream_velocity = 8
rho = 1.225
radius = 0.11
Area = np.pi * radius**2
# Area = 0.44**2

inlet_energy = 0.5 * rho * Area * (free_stream_velocity**3)

velocity = np.sqrt(np.sum(vel**2, axis=1))
mean_velocity = np.mean(velocity)

power = 0.5 * rho * Area * velocity**3

cp = 1 - (total_power / inlet_energy)

print(f"cp = {cp*100:.2f}%")
