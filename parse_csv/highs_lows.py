# -*- coding:utf-8 -*-
import csv 
from datetime import datetime

from matplotlib import pyplot as plt

#从文件中获取日期、最高温度、最低温度
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs, dates, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:    
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
#根据数据绘制图形
fig = plt.figure(dpi=100, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

#设置图形格式
plt.title("Daily high and lows temperatures - 2014", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

