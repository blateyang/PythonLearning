# ----------------------
# Author: blateyang
# Date: 2018/3/12
# ----------------------
"""Test random_random.py and visualize the process"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # create instance of random walk class and plot it out
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    # set figure size and resolution
    plt.figure(dpi=128, figsize=(10, 6))

    plt.scatter(rw.x_values, rw.y_values,
                c=point_numbers, cmap=plt.cm.Blues, s=15)
    # plt.plot(rw.x_values, rw.y_values, linewidth=2)
    # highlight the start point and end point
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    plt.axis('off')
    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
