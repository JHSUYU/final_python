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

#红葡各变量与评分关系
colnm = dfr.columns.tolist()[:12]
plt.figure(figsize = (10, 8))
for i in range(12):
    plt.subplot(4,3,i+1)
    sns.boxplot(x ='quality', y = colnm[i], data = dfr, color = color[1], width = 0.6)
    plt.ylabel(colnm[i],fontsize = 12)
plt.suptitle('红葡萄酒各变量与评分关系--箱线图', y=1.0, fontsize=14)
plt.tight_layout()
plt.show()

#白葡各变量与评分关系
colnm = dfw.columns.tolist()[:12]
plt.figure(figsize = (10, 8))
for i in range(12):
    plt.subplot(4,3,i+1)
    sns.boxplot(x ='quality', y = colnm[i], data = dfw, color = color[1], width = 0.6)
    plt.ylabel(colnm[i],fontsize = 12)
plt.suptitle('白葡萄酒各变量与评分关系--箱线图', y=1.0, fontsize=14)
plt.tight_layout()
plt.show()

#红葡热力相关图
plt.figure(figsize = (10,8))
colnm = dfr.columns.tolist()
mcorr = dfr[colnm].corr()
mask = np.zeros_like(mcorr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(mcorr, mask=mask, cmap=cmap, square=True, annot=True, fmt='0.2f')
plt.title('红葡萄酒各变量间热力相关图')
plt.show()

#白葡热力相关图
plt.figure(figsize = (10,8))
colnm = dfw.columns.tolist()
mcorr = dfw[colnm].corr()
mask = np.zeros_like(mcorr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(mcorr, mask=mask, cmap=cmap, square=True, annot=True, fmt='0.2f')
plt.title('白葡萄酒各变量间热力相关图')
plt.show()