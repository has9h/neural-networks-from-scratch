import matplotlib.pyplot as plt
import numpy as np 

# Equation format: y = -(b/a)x - (c/a)

# Enter coefficients & learning rate:
a = 3
b = 4
c = -10
alpha = 0.1
coord = (4, 5, 1)

# Step sizes:
step_y = alpha * coord[0]
step_x = alpha * coord[1]
step_bias = alpha * coord[2]

# Enter range for variables:
x = np.arange(-50, 50.2, 0.5)
# y = -((b/a) * x) - (c/a)

color = ['r', 'g', 'b', 'c', 'm', 'y', 'k', '#003300', '#00FF00', "#003F00", "#00CF00"]

for i in range(100):
    a -= step_y
    b -= step_x
    c -= step_bias

    print("{}y {}x {}".format(round(a, 2), round(b, 2), round(c, 2)))


# for i in range(0, 11):
#     # Set equation:
#     y = -(round((b/a), 2) * x) - round((c/a), 2)

#     plt.plot(x, y, color[i], label="{}y {}x {}".format(round(a, 2), round(b, 2), round(c, 2)))
#     plt.scatter(coord[0], coord[1])

#     # Set changing values:
#     a -= step_y
#     b -= step_x
#     c -= step_bias

# Plotting boilerplate:

plt.title("Basic Graph", fontdict={'fontsize': 8})
plt.xlabel('x-axis', fontdict={'fontsize': 8})
plt.ylabel('y-axis', fontdict={'fontsize': 8})

# plt.xticks(range(-50, 50, 2))
# plt.yticks([0, 2, 4, 6])

plt.legend()
plt.show()
