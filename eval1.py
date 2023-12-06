import point_cloud_utils as pcu
import numpy as np
import random
import matplotlib.pyplot as plt

def read_xyz_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        # Split each line into x, y, and z coordinates
        coordinates = [float(coord) for coord in line.split()]
        data.append(coordinates)

    # Convert the list of coordinates to a NumPy array
    np_array = np.array(data)

    return np_array

# Replace 'your_xyz_file.xyz' with the path to your XYZ file
xyz_file_path = 'escanor_axe.xyz'
numpy_array = read_xyz_file(xyz_file_path)
noisy_array=numpy_array.copy()

chamfer_errors=[]
hausdorff_errors=[]

error_range=51

for error in range(error_range):
    for i in range(len(noisy_array)):
        for j in range(3):
            noisy_array[i,j]=noisy_array[i,j]*random.randint(100-error,100+error)/100

    #np.savetxt("noisy_axe.csv", noisy_array, delimiter=',')
    chamfer_dist = pcu.chamfer_distance(noisy_array, numpy_array)
    hausdorff_dist = pcu.hausdorff_distance(noisy_array, numpy_array)
    chamfer_errors.append(chamfer_dist)
    hausdorff_errors.append(hausdorff_dist)
    #print(error,":",chamfer_dist,hausdorff_dist)


for i in range(len(chamfer_errors)):
    chamfer_errors[i]/=max(chamfer_errors)
for i in range(len(hausdorff_errors)):
    hausdorff_errors[i]/=max(hausdorff_errors)

plt.figure(1)
plt.plot(range(error_range), chamfer_errors)
plt.xlabel("Noise")
plt.ylabel("Predicted Distance")
plt.title("Chamfer Distance vs Noise")
plt.figure(2)
plt.plot(range(error_range), hausdorff_errors)
plt.xlabel("Noise")
plt.ylabel("Predicted Distance")
plt.title("Hausdorff Distance vs Noise")
plt.show()

