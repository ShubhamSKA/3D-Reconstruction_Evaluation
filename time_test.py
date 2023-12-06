import point_cloud_utils as pcu
import numpy as np
import time
import matplotlib.pyplot as plt

i=10
times=[]
points=[]
while (i<100000000):
    a = np.random.rand(i, 3)*(i/10)
    b = np.random.rand(i, 3)*(i/10)
    start_time=time.time()
    chamfer_dist=pcu.chamfer_distance(a,b)
    print("chamfer dist for i=",i, "is", chamfer_dist, "and it took", time.time()-start_time, "seconds to run")
    times.append(time.time()-start_time)
    points.append(i)
    i*=10

plt.plot(points,times)
plt.show()