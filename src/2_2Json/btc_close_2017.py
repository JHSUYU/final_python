import requests
import json
import pygal
import math
'''文件网络地址'''
json_url='https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
'''调用requests.get()方法读取获取文件内容存放在变量req中，得到的是字符串'''
req=requests.get(json_url)

with open('btc_close_2017.json', 'w') as f:
    f.write(req.text)  #向文件中写入req的内容
'''加载文件内容,req.json可以将文件内容转化成Python列表'''
file_requests=req.json()
import json
import pygal

filename = 'btc_close_2017.json'
with open(filename) as f:
	btc_date = json.load(f)
#创建五个列表
dates=[]
months=[]
weeks=[]
weekdays=[]
close=[]
#每一天的信息
for btc_dict in btc_date:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=22,show_minor_x_labels = False)
line_chart.title='收盘价变换（￥）'
line_chart.x_labels = dates
N=20#每隔20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价',close)
line_chart.render_to_file('收盘价折线图（￥）.svg')

