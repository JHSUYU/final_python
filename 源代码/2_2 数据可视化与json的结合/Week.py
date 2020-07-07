import json
import pygal
import math
from itertools import groupby

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_date = json.load(f)
# 创建五个列表
dates = []
months = []
weeks = []
weekdays = []
close = []
# 每一天的信息
for btc_dict in btc_date:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))


def draw_line(x_date, y_date, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_date, y_date)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        """ 与该行代码相等
		y_list=[]
			for _,v in y:
   			 	y_list.append(v)"""
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘价星期均值折线图（￥）', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值折线图（￥）.svg')
line_chart_weekday
