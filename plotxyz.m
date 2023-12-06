points=readmatrix("escanor_axe.csv");
figure(1)
plot3(points(:,1), points(:,2), points(:,3), ".")
axis equal

points2=readmatrix("noisy_axe.csv");
figure(2)
plot3(points2(:,1), points2(:,2), points2(:,3), ".")
axis equal

