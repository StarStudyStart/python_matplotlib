# -*-coding:utf-8 -*-
import requests
import json
import math
from itertools import groupby

import pygal
'''
#获取数据并写入文件中
json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"

req = requests.get(json_url)
#req.raise_for_status()
with open("btc_close_2017_request.json", 'w') as f:
    f.write(req.text)
file_requests = req.json()
'''
#从文件中读数据并且加载到一个列表中
file_name = "btc_close_2017request.json"
with open(file_name) as f:
    btc_data = json.load(f)
    
#创建5个列表分别存储日期和收盘价
dates = []
months =[]
weeks =[]
weekdays = []
close = []

#打印每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict.get("date"))
    months.append(int(btc_dict.get("month"))) 
    weeks.append(int(btc_dict.get("week")))
    weekdays.append(btc_dict.get("weekday"))
    close.append(int(float(btc_dict.get("close"))))  #带有浮点数的字符串不能直接转换为整型，需要先转换为浮点型 例：“34343.3434”
    #print("{} is month {} week {},{} the close price is {} RMB".format(date,
    #    month, week, weekday, close))

#绘制收盘折线图    
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换（￥）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换（￥）.svg')

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _ : _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart
    
idx_month = dates.index('2017-12-01')
draw_line(months[:idx_month], close[:idx_month], '收盘月日均值（￥）','月日均值' )

idx_week = dates.index('2017-12-11')
draw_line(weeks[1:idx_week], close[1:idx_week], '收盘周日均值（￥）', '周日均值')

wd = ['Monday', 'Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
wd_hans = ['周一', '周二','周三','周四', '周五', '周六', '周日']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘星期均值（￥）', '星期均值')
line_chart_weekday.x_labels = wd_hans 
line_chart_weekday.render_to_file('收盘星期均值（￥）.svg')

def make_dashboard():
    with open('收盘价DashBoard.html', 'w', encoding='utf-8') as html_file:
        html_file.write('<html><head><title>收盘价DashBoard</title><meta charset="utf-8"></head><body>\n')
        for svg in ['收盘价（￥）.svg', '收盘价对数变换（￥）.svg', '收盘月日均值（￥）.svg',
            '收盘周日均值（￥）.svg', '收盘星期均值（￥）.svg']:
            html_file.write('   <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')
        
make_dashboard()
            
