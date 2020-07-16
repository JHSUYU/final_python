#coding=utf-8
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

#1.初始化一个线性矩阵并求秩
M = np.array([[1,2],[2,4]])   #初始化一个2*2的线性相关矩阵
np.linalg.matrix_rank(M,tol=None)  # 计算矩阵的秩

#2.读取训练数据与测试数据集。
digits_train = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra', header=None)
digits_test = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes', header=None)
print (digits_train.shape)   #(3823, 65)    3000+个样本，每个数据由64个特征，1个标签构成
print (digits_test.shape)   #(1797, 65)

#3将数据降维到2维并可视化

# 3.1 分割训练数据的特征向量和标记
X_digits = digits_train[np.arange(64)]         #得到64位特征值
y_digits = digits_train[64]                    #得到对应的标签

#3.2 PCA降维：降到2维
estimator = PCA(n_components=2)
X_pca=estimator.fit_transform(X_digits)

#3.3 显示这10类手写体数字图片经PCA压缩后的2维空间分布
def plot_pca_scatter():
    colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
    for i in range(len(colors)):
        px = X_pca[:, 0][y_digits.values == i]
        py = X_pca[:, 1][y_digits.values == i]
        plt.scatter(px, py, c=colors[i])
    plt.legend(np.arange(0, 10).astype(str))
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.show()
plot_pca_scatter()

