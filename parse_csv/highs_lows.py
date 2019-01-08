# -*- coding:utf-8 -*-
import csv 

from matplotlib import pyplot as plt

#从文件中获取最高温度
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = [int(row[1]) for row in reader]
    print(highs)

#根据数据绘制图形
fig = plt.figure(dpi=100, figsize=(10, 6))
plt.plot(highs, linewidth=5, c='red')

#设置图形格式
plt.title("Daily high temperatures, july 2014", fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

