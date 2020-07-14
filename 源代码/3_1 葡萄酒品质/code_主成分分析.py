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

#输入变量主成分分析
"""
参数：
    - XMat：传入的是一个numpy的矩阵格式，行表示样本数，列表示特征
    - k：表示取前k个特征值对应的特征向量
函数解释：
    - pca_mat()：获取参与运算的多维数组
    - pca_eig()：返回满足要求的前k个特征值和特征向量
    - pca_coe()：返回主成分系数
    - pca()：返回每个样本的主成分得分
    - pca_draw()：返回前两个主成分得分的散点图
"""
def pca_mat(x):
    temp = x.drop(['quality','total acidity'],axis=1) #获取去除评分项的数据表
    XMat = np.array(temp) #dataframe格式转为多维数组
    average = np.mean(XMat,axis=0) #axis=0表示按照列来求均值
    standard = np.std(XMat,axis=0) #求每列标准差
    data_adjust = (XMat - average)/standard #中心标准化
    return data_adjust

def pca_eig(data_adjust):
    covmat = np.cov(data_adjust, rowvar=0)   #计算协方差矩阵
    eigVals,eigVects = np.linalg.eig(covmat)  #求解协方差矩阵的特征值和特征向量
    eigValInd = np.argsort(-eigVals) #按照eigVals进行从大到小排序（给出序号，不修改原特征值列表）
    """确定前k的主成分，使选取的主成分贡献90%以上的方差"""
    val_sum = 0
    val_total = eigVals.sum()
    for k in eigValInd:
        val_sum += eigVals[k]
        if val_sum/val_total < 0.90:
            continue
        else:
            break
    """分割线"""
    x = int(np.argwhere(eigValInd==k)+1) #定位k所在位置，结果加1
    eigValInd = eigValInd[:x:1] #截取前k个特征值的序号
    """取前k特征值"""
    list = []
    for i in eigValInd:
        list.append(eigVals[i])
    redEigVals = np.array(list)
    """对应前k的特征向量"""
    redEigVects = []
    for i in eigValInd:
        redEigVects.append(eigVects[i])
    redEigVects = np.array(redEigVects).T
    return redEigVals, redEigVects, eigVals, eigVects

def pca_coe(data_adjust):
    return pca_eig(data_adjust)[1]/(pca_eig(data_adjust)[0]**0.5)

def pca(data_adjust):
    lowDDataMat = np.matrix(data_adjust) * pca_eig(data_adjust)[1]
    return lowDDataMat

def pca_draw(data_adjust):
    df = pd.DataFrame(pca(data_adjust))
    plt.scatter(x=df[0], y=df[1])
    if data_adjust.sum() - pca_mat(dfr).sum() == 0:
        i = '红葡萄酒'
    else:
        i = '白葡萄酒'
    plt.title(f'{i}'+'主成分得分--散点图')
    plt.xlabel('第一主成分', fontsize=12)
    plt.ylabel('第二主成分', fontsize=12)
    plt.show()

"""红、白葡萄酒初始分析数据"""
pr = pca_mat(dfr)
pw = pca_mat(dfw)

"""主成分分析"""
pca_eig(pr)[2]
pca_eig(pw)[2]

pca_eig(pr)[0]
pca_eig(pw)[0]

"""主成分系数 解释为第K个主成分表示为11个输入变量的线性组合。可见很难清晰的描述除各主成分代表的含义。"""
pd.DataFrame(pca_coe(pr))
pd.DataFrame(pca_coe(pw))

"""主成分得分 解释为每个样本点在主成分上投影的坐标。"""
pd.DataFrame(pca(pr))
pd.DataFrame(pca(pw))

"""主成分得分散点图"""
pca_draw(pr)
pca_draw(pw)