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
# 以上全是基本配置，新建文件需要复制

# print(dfr.head())

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

# 红葡单变量箱线图
colnum_red = dfr.columns.tolist()
plt.figure(figsize=(10, 6), dpi=200)
plt.suptitle('红葡萄酒单变量箱线图', y=1.00, fontproperties=my_font)  # 总标题
# 画第一行的图
for i in range(7):
    plt.subplot(2, 7, i + 1)
    sns.boxplot(dfr[colnum_red[i]], orient="v", width=0.4, color=color[0])
    plt.ylabel(colnum_red[i], fontsize=12)
plt.tight_layout()
# 画第二行的图
for i in range(6):
    plt.subplot(2, 6, i + 7)
    sns.boxplot(dfr[colnum_red[i + 7]], orient="v", width=0.4, color=color[0])
    plt.ylabel(colnum_red[i + 7], fontsize=12)
plt.tight_layout()
plt.show()


# 白葡单变量箱线图
colnum_white = dfw.columns.tolist()
plt.figure(figsize=(10, 6))
plt.suptitle('白葡萄酒单变量箱线图', y=1.00, fontproperties=my_font)  # 总标题
# 画第一行的图
for i in range(7):
    plt.subplot(2, 7, i + 1)
    sns.boxplot(dfw[colnum_white[i]], orient="v", width=0.4, color=color[0])
    plt.ylabel(colnum_white[i], fontsize=12)
plt.tight_layout()
# 画第二行的图
for i in range(6):
    plt.subplot(2, 6, i + 7)
    sns.boxplot(dfw[colnum_white[i + 7]], orient="v", width=0.4, color=color[0])
    plt.ylabel(colnum_white[i + 7], fontsize=12)
plt.tight_layout()
plt.show()


