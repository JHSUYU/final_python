import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager

dfr = pd.read_csv(r'winequality-red.csv', sep=';')
dfw = pd.read_csv(r'winequality-white.csv', sep=';')

# 颜色
color = sns.color_palette()
# 数据print精度
pd.set_option('precision', 3)
# 显示完整的列
pd.set_option('display.max_columns', None)
# 显示完整的行
pd.set_option('display.max_rows', None)
# 设置字体
my_font = font_manager.FontProperties(fname="苹方字体.ttf")

# 增加总酸
dfr['total acid'] = dfr['fixed acidity'] + dfr['volatile acidity']
dfw['total acid'] = dfw['fixed acidity'] + dfw['volatile acidity']
# 移动dfr总酸到列首
r = dfr.columns.tolist()
r.insert(0, r.pop())
dfr = dfr.reindex(columns=r)
# 移动dfw总酸到列首
r = dfw.columns.tolist()
r.insert(0, r.pop())
dfw = dfw.reindex(columns=r)

# print(dfr.head())

colnm = dfr.columns.tolist()
plt.figure(figsize = (20, 15))
plt.suptitle("红葡萄酒单变量直方图\nY轴：频数", y=1.0, fontsize = 16) #总标题
# 画前三行的图
for i in range(9):
    plt.subplot(4,3,i+1)
    dfr[colnm[i]].hist(bins = 100, color = color[3])
    plt.xlabel(colnm[i],fontsize = 14)
plt.tight_layout()
# 画第四行的图
for i in range(4):
    plt.subplot(4,4,i+13)
    dfr[colnm[i+9]].hist(bins = 100, color = color[3])
    plt.xlabel(colnm[i+9],fontsize = 14)
plt.tight_layout()
plt.show()

#白葡单变量直方图
colnm = dfw.columns.tolist()
plt.figure(figsize = (16, 12))
plt.suptitle('白葡萄酒单变量直方图\nY轴：频数', y=1, fontsize = 16) #总标题
"""画前三行的图"""
for i in range(9):
    plt.subplot(4,3,i+1)
    dfw[colnm[i]].hist(bins = 100, color = color[4])
    plt.xlabel(colnm[i],fontsize = 14)
plt.tight_layout()
"""画第四行的图"""
for i in range(4):
    plt.subplot(4,4,i+13)
    dfw[colnm[i+9]].hist(bins = 100, color = color[4])
    plt.xlabel(colnm[i+9],fontsize = 14)
plt.tight_layout()
plt.show()
