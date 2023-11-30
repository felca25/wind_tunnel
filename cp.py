import numpy as np
# from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile

# Load OpenFOAM controlDict to get simulation parameters
# controlDict = ParsedParameterFile("steady/system/controlDict")
rho = 1.225

# Load velocity and pressure fields
U = np.loadtxt("steady/postProcessing/0.00525/0/U", skiprows=23)[:, 3:]
p = np.loadtxt("steady/postProcessing/0.00525/0/p", skiprows=23)[:, 3:]

# Calculate power
A = np.pi * (0.22**2)# Calculate your rotor swept area
P = np.sum(0.5 * rho * U[:, 0] * (U[:, 1:] + p[:, 1:]), axis=1)

# Calculate Cp
U_ref = 8 # Your reference wind speed
Cp = P / (0.5 * rho * A * U_ref**3)

# Save or further process Cp values
np.savetxt("Cp_values.txt", Cp)
