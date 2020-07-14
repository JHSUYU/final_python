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

# 固定酸占总酸比重
plt.suptitle('固定酸占总酸比分布情况', y=1.00, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
temp = dfr[{'total acidity', 'fixed acidity'}]
temp['precent'] = temp.apply(lambda x: x['fixed acidity'] / x['total acidity'], axis=1)  # 计算占比
temp['precent'].hist(bins=100, color=color[0])
plt.xlabel('红葡萄酒固定酸占比', fontsize=12, fontproperties=my_font)
plt.ylabel('频数', fontsize=12, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
temp = dfw[{'total acidity', 'fixed acidity'}]
temp['precent'] = temp.apply(lambda x: x['fixed acidity'] / x['total acidity'], axis=1)  # 计算占比
temp['precent'].hist(bins=100, color=color[0])
plt.xlabel('白葡萄酒固定酸占比', fontsize=12, fontproperties=my_font)
plt.ylabel('频数', fontsize=12, fontproperties=my_font)
plt.show()


# 固定酸占比对评分影响
plt.suptitle('固定酸占总酸比对评分的影响', y=1.00, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
temp = dfr[{'total acidity', 'fixed acidity', 'quality'}]
temp['precent'] = temp.apply(lambda x: x['fixed acidity'] / x['total acidity'], axis=1)  # 计算占比
sns.boxplot(x=temp['quality'], y=temp['precent'])
plt.xlabel('红葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('固定酸占比', fontsize=12, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
temp = dfw[{'total acidity', 'fixed acidity', 'quality'}]
temp['precent'] = temp.apply(lambda x: x['fixed acidity'] / x['total acidity'], axis=1)  # 计算占比
sns.boxplot(x=temp['quality'], y=temp['precent'])
plt.xlabel('白葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('固定酸占比', fontsize=12, fontproperties=my_font)
plt.show()

# 柠檬酸占固定酸比重
plt.suptitle('柠檬酸占固定酸比分布情况', y=1.00, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
temp = dfr[{'citric acid', 'fixed acidity'}]
temp['precent'] = temp.apply(lambda x: x['citric acid'] / x['fixed acidity'], axis=1)  # 计算占比
temp['precent'].hist(bins=100, color=color[0])
plt.xlabel('红葡萄酒柠檬酸占比', fontsize=12, fontproperties=my_font)
plt.ylabel('频数', fontsize=12, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
temp = dfw[{'citric acid', 'fixed acidity'}]
temp['precent'] = temp.apply(lambda x: x['citric acid'] / x['fixed acidity'], axis=1)  # 计算占比
temp['precent'].hist(bins=100, color=color[0])
plt.xlabel('白葡萄酒柠檬酸占比', fontsize=12, fontproperties=my_font)
plt.ylabel('频数', fontsize=12, fontproperties=my_font)
plt.show()

# 柠檬酸占比对评分影响
plt.suptitle('柠檬酸占固定酸比对评分的影响', y=1.00, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
temp = dfr[{'citric acid', 'fixed acidity', 'quality'}]
temp['precent'] = temp.apply(lambda x: x['citric acid'] / x['fixed acidity'], axis=1)  # 计算占比
sns.boxplot(x=temp['quality'], y=temp['precent'])
plt.xlabel('红葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('柠檬酸占比', fontsize=12, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
temp = dfw[{'citric acid', 'fixed acidity', 'quality'}]
temp['precent'] = temp.apply(lambda x: x['citric acid'] / x['fixed acidity'], axis=1)  # 计算占比
sns.boxplot(x=temp['quality'], y=temp['precent'])
plt.xlabel('白葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('柠檬酸占比', fontsize=12, fontproperties=my_font)
plt.show()

# 挥发酸占总酸比重
plt.suptitle('挥发酸占总酸比分布情况', y=1.00, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
temp = dfr[{'total acidity', 'volatile acidity'}]
temp['precent'] = temp.apply(lambda x: x['volatile acidity'] / x['total acidity'], axis=1)  # 计算占比
temp['precent'].hist(bins=100, color=color[0])
plt.xlabel('红葡萄酒挥发酸占比', fontsize=12, fontproperties=my_font)
plt.ylabel('频数', fontsize=12, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
temp = dfw[{'total acidity', 'volatile acidity'}]
temp['precent'] = temp.apply(lambda x: x['volatile acidity'] / x['total acidity'], axis=1)  # 计算占比
temp['precent'].hist(bins=100, color=color[0])
plt.xlabel('白葡萄酒挥发酸占比', fontsize=12, fontproperties=my_font)
plt.ylabel('频数', fontsize=12, fontproperties=my_font)
plt.show()

# 挥发酸占比对评分影响
plt.suptitle('挥发酸占总酸比对评分的影响', y=1.00, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
temp = dfr[{'total acidity', 'volatile acidity', 'quality'}]
temp['precent'] = temp.apply(lambda x: x['volatile acidity'] / x['total acidity'], axis=1)  # 计算占比
sns.boxplot(x=temp['quality'], y=temp['precent'])
plt.xlabel('红葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('挥发酸占比', fontsize=12, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
temp = dfw[{'total acidity', 'volatile acidity', 'quality'}]
temp['precent'] = temp.apply(lambda x: x['volatile acidity'] / x['total acidity'], axis=1)  # 计算占比
sns.boxplot(x=temp['quality'], y=temp['precent'])
plt.xlabel('白葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('挥发酸占比', fontsize=12, fontproperties=my_font)
plt.show()

# 总酸对评分影响
plt.suptitle('总酸含量对评分的影响', y=1.00, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
temp = dfr[{'total acidity', 'quality'}]
sns.boxplot(x=temp['quality'], y=temp['total acidity'])
plt.xlabel('红葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('总酸含量', fontsize=12, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
temp = dfw[{'total acidity', 'quality'}]
sns.boxplot(x=temp['quality'], y=temp['total acidity'])
plt.xlabel('白葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('总酸含量', fontsize=12, fontproperties=my_font)
plt.show()

# pH对评分影响
plt.suptitle('pH值对评分的影响', y=1.00, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
temp = dfr[{'pH', 'quality'}]
sns.boxplot(x=temp['quality'], y=temp['pH'])
plt.xlabel('红葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('pH值', fontsize=12, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
temp = dfw[{'pH', 'quality'}]
sns.boxplot(x=temp['quality'], y=temp['pH'])
plt.xlabel('白葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('pH值', fontsize=12, fontproperties=my_font)
plt.show()

# 按柠檬酸分类
plt.suptitle('按柠檬酸含量分类', y=1.00, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
temp = pd.cut(dfr['citric acid'], bins=[-0.1, 1, 2], labels=["干、半干、半甜", "甜"])
temp = pd.DataFrame(temp)
temp['citric acid'].value_counts().plot(kind='bar')
num = temp['citric acid'].value_counts()
for x, y in enumerate(num.values):
    plt.text(x, y, "%s" % y, ha='center', va='bottom')  # 显示数字
plt.xticks(rotation=360, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
temp = pd.cut(dfw['citric acid'], bins=[-0.1, 1, 2.1], labels=["干、半干、半甜", "甜"])
temp = pd.DataFrame(temp)
temp['citric acid'].value_counts().plot(kind='bar')
num = temp['citric acid'].value_counts()
for x, y in enumerate(num.values):
    plt.text(x, y, "%s" % y, ha='center', va='bottom')  # 显示数字
plt.xticks(rotation=360, fontproperties=my_font)
plt.show()

