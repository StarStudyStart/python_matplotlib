# -*-coding:utf-8 -*-

import requests

#执行API 并存储响应

url = 'http://wthrcdn.etouch.cn/weather_mini?city=北京'
r = requests.get(url)
r.encoding = r.apparent_encoding
print("Status Code:", r.status_code)
print(r.json())
#提取所需数据，进行存储
high, low = [], []
#数据可视化处理