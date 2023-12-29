import numpy as np

for i in range(0,6):
    with open(f"steady/processor{i}/1760/k", 'r') as f:
        data = f.readlines()
        k = np.array(np.float32(data[21:-9]))
        # print(len(data))
        # print(data[-1])
    with open(f"steady/processor{i}/1760/omega", 'r') as f:
        omega = f.readlines()
        omega = np.array(np.float32(omega[21:-9]))
        # print(len(data))
        # print(data[-1])
    with open(f"steady/processor{i}/1760/p", 'w') as f:
        for line in data[:11]:
            f.write(line)
        f.write("    object      epsilon;\n")
        for line in data[12:20]:
            f.write(line)
        # f.write(data[13:20])
        # epsilon = k/omega 
        for i,w in enumerate(omega):
            e = k[i]/w
            f.write(f"{e:.8f}\n")
        for line in data[-9:]:
            f.write(line)
        # f.write(data[-9:])
        