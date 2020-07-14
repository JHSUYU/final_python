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

# 残留糖对评分影响
plt.suptitle('残留糖含量对评分的影响', y=1, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
sns.boxplot(x=dfr['quality'], y=dfr['residual sugar'])
plt.xlabel('红葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('残留糖含量', fontsize=12, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
sns.boxplot(x=dfw['quality'], y=dfw['residual sugar'])
plt.xlabel('白葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('残留糖含量', fontsize=12, fontproperties=my_font)
plt.show()

# 按残留糖含量分类
plt.suptitle('按残留糖含量分类', y=1.0, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
temp = pd.cut(dfr['residual sugar'], bins=[-0.1, 4, 12, 45, 100], labels=["干", "半干", "半甜", "甜"])
temp = pd.DataFrame(temp)
temp['residual sugar'].value_counts().plot(kind='bar')
num = temp['residual sugar'].value_counts()
for x, y in enumerate(num.values):
    plt.text(x, y, "%s" % y, ha='center', va='bottom')
plt.xticks(rotation=360, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
temp = pd.cut(dfw['residual sugar'], bins=[-0.1, 4, 12, 45, 100], labels=["干", "半干", "半甜", "甜"])
temp = pd.DataFrame(temp)
temp['residual sugar'].value_counts().plot(kind='bar')
num = temp['residual sugar'].value_counts()
for x, y in enumerate(num.values):
    plt.text(x, y, "%s" % y, ha='center', va='bottom')
plt.xticks(rotation=360, fontproperties=my_font)
plt.show()
