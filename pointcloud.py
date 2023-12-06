import point_cloud_utils as pcu
import numpy as np
import matplotlib.pyplot as plt


# a and b are arrays where each row contains a point
# Note that the point sets can have different sizes (e.g [100, 3], [111, 3])
a = np.random.rand(10000, 3)
b = np.random.rand(10000, 3)
c = np.random.rand(10000, 3)
d=b*1.1
e=b*0.9

chamfer_dist = pcu.chamfer_distance(a, b)
print("a   ",chamfer_dist)
chamfer_dist = pcu.chamfer_distance(2*a, b)
print("2a  ",chamfer_dist)
chamfer_dist = pcu.chamfer_distance(c, b)
print("c   ",chamfer_dist)
chamfer_dist = pcu.chamfer_distance(d, b)
print("1.1b",chamfer_dist)
chamfer_dist = pcu.chamfer_distance(e, b)
print("0.9b",chamfer_dist)

range_distances=[]
for i in range(0, 50):
    chamfer_dist = pcu.chamfer_distance(i*a/10, b)
    range_distances.append(chamfer_dist)


plt.figure(1)
plt.plot(range(0,50), range_distances)

range_distances2=[]

for i in range(0, 50):
    chamfer_dist = pcu.chamfer_distance(i*b/10, b)
    range_distances2.append(chamfer_dist)
plt.figure(2)
plt.plot(range(0,50), range_distances2)
plt.show()
