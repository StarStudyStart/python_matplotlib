# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt 
from random_walk import RandomWalk

#只要程序处于活动状态，就不停的模拟随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues,
        edgecolor='none', s=1)
        
    #突出起点和重点
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
        s=100)
    plt.show()
    
    keep_running = input("Make another walk?(y/n): ")
    if keep_running == "n":
        break