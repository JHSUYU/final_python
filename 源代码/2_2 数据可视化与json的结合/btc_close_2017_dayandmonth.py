import json
import pygal
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


idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值（￥）', '月日均值')
line_chart_month
