# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4]
squares = [1, 4, 9, 16]
plt.plot(input_values, squares, linewidth=5)

#设置图表标题，并给坐标加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of size", fontsize=14)

#设置刻度标记
plt.tick_params(axis='both', labelsize=14)
plt.show()
