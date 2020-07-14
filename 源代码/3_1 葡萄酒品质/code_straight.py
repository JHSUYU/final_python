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
plt.figure(figsize=(16, 20))
plt.suptitle("红葡萄酒单变量直方图\nY轴：频数", y=1.0, fontsize=16, fontproperties=my_font)  # 总标题
# 画前三行的图
for i in range(9):
    plt.subplot(4, 3, i + 1)
    dfr[colnm[i]].hist(bins=100, color=color[3])
    plt.xlabel(colnm[i], fontsize=14)
plt.tight_layout()
# 画第四行的图
for i in range(4):
    plt.subplot(4, 4, i + 13)
    dfr[colnm[i + 9]].hist(bins=100, color=color[3])
    plt.xlabel(colnm[i + 9], fontsize=14)
plt.tight_layout()
plt.show()

# 白葡单变量直方图
colnm = dfw.columns.tolist()
plt.figure(figsize=(16, 20))
plt.suptitle('白葡萄酒单变量直方图\nY轴：频数', y=1, fontsize=16, fontproperties=my_font)  # 总标题
"""画前三行的图"""
for i in range(9):
    plt.subplot(4, 3, i + 1)
    dfw[colnm[i]].hist(bins=100, color=color[4])
    plt.xlabel(colnm[i], fontsize=14)
plt.tight_layout()
"""画第四行的图"""
for i in range(4):
    plt.subplot(4, 4, i + 13)
    dfw[colnm[i + 9]].hist(bins=100, color=color[4])
    plt.xlabel(colnm[i + 9], fontsize=14)
plt.tight_layout()
plt.show()

# 红白变量箱线图
colnm_r = dfr.columns.tolist()
colnm_w = dfw.columns.tolist()
plt.figure(figsize=(10, 6))
plt.suptitle('单变量直方图对比', fontsize=14, y=1.05, fontproperties=my_font)  # 总标题
"""画前三行的图"""
for i in range(9):
    y1 = dfr[colnm_r[i]].tolist()
    y2 = dfw[colnm_w[i]].tolist()
    data = []
    data.append(y1)
    data.append(y2)
    plt.subplot(4, 3, i + 1)
    plt.hist(data, bins=100, histtype='bar')
    plt.legend(['红', '白'], prop=my_font)
    plt.xlabel(colnm_r[i], fontsize=12)
plt.tight_layout()
"""画第四行的图"""
for i in range(4):
    y1 = dfr[colnm_r[i + 9]].tolist()
    y2 = dfw[colnm_w[i + 9]].tolist()
    data = []
    data.append(y1)
    data.append(y2)
    plt.subplot(4, 4, i + 13)
    plt.hist(data, bins=100, histtype='bar')
    plt.legend(['红', '白'], prop=my_font)
    plt.xlabel(colnm_r[i + 9], fontsize=14)
plt.tight_layout()
plt.show()
