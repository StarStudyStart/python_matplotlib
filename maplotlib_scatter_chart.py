# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
#plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues,
    edgecolor='none', s=40)

#设置标题并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#设置坐标轴的取值范围
plt.axis([0,1000, 0, 1100000])
plt.show()