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

# 酒精浓度对评分影响
plt.suptitle('酒精浓度对评分的影响', y=1.0, fontsize=16, fontproperties=my_font)  # 总标题
"""红"""
plt.subplot(1, 2, 1)
sns.boxplot(x=dfr['quality'], y=dfr['alcohol'])
plt.xlabel('红葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('酒精浓度', fontsize=12, fontproperties=my_font)
"""白"""
plt.subplot(1, 2, 2)
sns.boxplot(x=dfw['quality'], y=dfw['alcohol'])
plt.xlabel('白葡萄酒评分', fontsize=12, fontproperties=my_font)
plt.ylabel('酒精浓度', fontsize=12, fontproperties=my_font)
plt.show()

# 对于国际标准按国标标准，葡萄酒酒精浓度应不低于7.0，此处按这个标椎做一下检查，如果为0说明结果正常
(dfr[dfr['alcohol'] < 7]).alcohol.count()
(dfw[dfw['alcohol'] < 7]).alcohol.count()
