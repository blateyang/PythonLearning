# ----------------------
# Author: blateyang
# Date: 2018/3/12
# ----------------------
"""Simple exercises of matplotlib in Chapter 15"""

import matplotlib.pyplot as plt

# # plot simple line graph with plt.plot()
# index = list(range(1, 6))
# square_num = [1, 4, 9, 16, 25]
# plt.plot(index, square_num, linewidth=5)
# plt.xlabel('Value')
# plt.ylabel('Square of value')
# plt.title('Square Number', fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

# plot scatter graph with plt.scatter()
x_values = list(range(1, 1001, 100))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)
plt.axis([0, 1100, 0, 1100000])
plt.xlabel('Value')
plt.ylabel('Square of value')
plt.title('Square Number', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
