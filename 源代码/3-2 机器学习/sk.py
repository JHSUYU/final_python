from sklearn.datasets import load_iris           #导入数据集
from sklearn.decomposition import PCA            #导入函数库
import matplotlib.pyplot as plt
import numpy as np
iris=load_iris()
pca=PCA(n_components=2)                           #设置保留的主成分个数为2
trans_data=pca.fit_transform(iris.data)           #调用fit_transform方法，返回新的数据集
index1=np.where(iris.target==0)
index2=np.where(iris.target==1)
index3=np.where(iris.target==2)
labels=['setosa', 'versicolor', 'virginica']
plt.plot(trans_data[index1][:,0],trans_data[index1][:,1],'r*')
plt.plot(trans_data[index2][:,0],trans_data[index2][:,1],'g*')
plt.plot(trans_data[index3][:,0],trans_data[index3][:,1],'b*')
plt.legend(labels)
plt.show()


