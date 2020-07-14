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
# 设置图片大小
plt.figure(figsize=(10, 6), dpi=200)
# 设置字体
my_font = font_manager.FontProperties(fname="苹方字体.ttf")

# 增加总酸
dfr['total acidity'] = dfr['fixed acidity'] + dfr['volatile acidity']
dfw['total acidity'] = dfw['fixed acidity'] + dfw['volatile acidity']
# 移动dfr总酸到列首
r = dfr.columns.tolist()
r.insert(0, r.pop())
dfr = dfr.reindex(columns=r)
# 移动dfw总酸到列首
r = dfw.columns.tolist()
r.insert(0, r.pop())
dfw = dfw.reindex(columns=r)

#红葡密度与酒精
plt.figure(figsize = (6,4))
sns.regplot(x='density', y = 'alcohol', data = dfr, scatter_kws = {'s':10}, color = color[0])
plt.title('红葡萄酒密度与酒精的相关关系')
plt.show()

#红葡密度与酒精
plt.figure(figsize = (6,4))
sns.regplot(x='density', y = 'alcohol', data = dfw, scatter_kws = {'s':10}, color = color[0])
plt.title('白葡萄酒密度与酒精的相关关系')
plt.show()

#红葡糖与酒精
plt.figure(figsize = (6,4))
sns.regplot(x='residual sugar', y = 'alcohol', data = dfr, scatter_kws = {'s':10}, color = color[0])
plt.title('红酒残留糖与酒精的相关关系')
plt.show()

#白葡糖与酒精
plt.figure(figsize = (6,4))
sns.regplot(x='residual sugar', y = 'alcohol', data = dfw, scatter_kws = {'s':10}, color = color[0])
plt.title('白葡萄酒残留糖与酒精的相关关系')
plt.show()