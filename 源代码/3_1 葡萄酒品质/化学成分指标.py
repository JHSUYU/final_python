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

#氯化物浓度对评分影响
plt.figure(figsize = (10,4))
plt.suptitle('氯化物浓度对评分的影响', y=1.02, fontsize = 16) #总标题
"""红"""
plt.subplot(1,2,1)
sns.boxplot(x=dfr['quality'], y=dfr['chlorides'])
plt.xlabel('红葡萄酒评分',fontsize = 12)
plt.ylabel('氯化物浓度',fontsize = 12)
"""白"""
plt.subplot(1,2,2)
sns.boxplot(x=dfw['quality'], y=dfw['chlorides'])
plt.xlabel('白葡萄酒评分',fontsize = 12)
plt.ylabel('氯化物浓度',fontsize = 12)
plt.show()

#硫酸盐浓度对评分影响
plt.figure(figsize = (10,4))
plt.suptitle('硫酸盐浓度对评分的影响', y=1.0, fontsize = 16) #总标题
"""红"""
plt.subplot(1,2,1)
sns.boxplot(x=dfr['quality'], y=dfr['sulphates'])
plt.xlabel('红葡萄酒评分',fontsize = 12)
plt.ylabel('硫酸盐浓度',fontsize = 12)
"""白"""
plt.subplot(1,2,2)
sns.boxplot(x=dfw['quality'], y=dfw['sulphates'])
plt.xlabel('白葡萄酒评分',fontsize = 12)
plt.ylabel('硫酸盐浓度',fontsize = 12)
plt.show()

#游离二氧化硫占总二氧化硫比重
plt.figure(figsize = (10,4))
plt.suptitle('游离二氧化硫占总二氧化硫比重分布情况', y=1.0, fontsize = 16) #总标题
"""红"""
plt.subplot(1,2,1)
temp = dfr[{'free sulfur dioxide','total sulfur dioxide'}]
temp['precent'] = temp.apply(lambda x: x['free sulfur dioxide']/x['total sulfur dioxide'], axis=1) #计算占比
temp['precent'].hist(bins = 100, color = color[0])
plt.xlabel('红葡萄酒游离二氧化硫占比',fontsize = 12)
plt.ylabel('频数',fontsize = 12)
"""白"""
plt.subplot(1,2,2)
temp = dfw[{'free sulfur dioxide','total sulfur dioxide'}]
temp['precent'] = temp.apply(lambda x: x['free sulfur dioxide']/x['total sulfur dioxide'], axis=1) #计算占比
temp['precent'].hist(bins = 100, color = color[0])
plt.xlabel('白葡萄酒游离二氧化硫占比',fontsize = 12)
plt.ylabel('频数',fontsize = 12)
plt.show()

#游离二氧化硫占比对评分影响
plt.figure(figsize = (10,4))
plt.suptitle('游离二氧化硫占总二氧化硫比重对评分的影响', y=1.0, fontsize = 16) #总标题
"""红"""
plt.subplot(1,2,1)
temp = dfr[{'free sulfur dioxide','total sulfur dioxide','quality'}]
temp['precent'] = temp.apply(lambda x: x['free sulfur dioxide']/x['total sulfur dioxide'], axis=1)
sns.boxplot(x=temp['quality'], y=temp['precent'])
plt.xlabel('红葡萄酒评分',fontsize = 12)
plt.ylabel('游离二氧化硫占比',fontsize = 12)
"""白"""
plt.subplot(1,2,2)
temp = dfw[{'free sulfur dioxide','total sulfur dioxide','quality'}]
temp['precent'] = temp.apply(lambda x: x['free sulfur dioxide']/x['total sulfur dioxide'], axis=1)
sns.boxplot(x=temp['quality'], y=temp['precent'])
plt.xlabel('白葡萄酒评分',fontsize = 12)
plt.ylabel('游离二氧化硫占比',fontsize = 12)
plt.show()

#二氧化硫总量对评分影响
plt.figure(figsize = (10,4))
plt.suptitle('二氧化硫总量对评分的影响', y=1.0, fontsize = 16) #总标题
"""红"""
plt.subplot(1,2,1)
sns.boxplot(x=dfr['quality'], y=dfr['total sulfur dioxide'])
plt.xlabel('红葡萄酒评分',fontsize = 12)
plt.ylabel('二氧化硫总量',fontsize = 12)
"""白"""
plt.subplot(1,2,2)
sns.boxplot(x=dfw['quality'], y=dfw['total sulfur dioxide'])
plt.xlabel('白葡萄酒评分',fontsize = 12)
plt.ylabel('二氧化硫总量',fontsize = 12)
plt.show()


