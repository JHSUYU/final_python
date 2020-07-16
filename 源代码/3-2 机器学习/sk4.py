import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import preprocessing
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn import metrics
from sklearn import random_projection
from sklearn import manifold
from sklearn import decomposition

##乳腺癌数据集
X,y=datasets.load_breast_cancer(return_X_y=True)
##print("X.shape:",X.shape)
##print("y.shape:",y.shape)
##print("X[:3]:",X[:3])
##print("y[:3]",y[:3])

##随机投影降维
##rp=random_projection.SparseRandomProjection(n_components=3,density=0.1,random_state=0)
##X_projected=rp.fit_transform(X)

##T-SNE降维
tsne=manifold.TSNE(n_components=3,init="pca")
X_projected=tsne.fit_transform(X)

##PCA降维
##pca=decomposition.TruncatedSVD(n_components=3)
##X_projected=pca.fit_transform(X)

##Isomap降维
##iso = manifold.Isomap(n_neighbors=20, n_components=3)
#X_projected=iso.fit_transform(X)

##结果标准化
##X_projected=preprocessing.scale(X_projected)

##DBSCAN聚类
##y_pred=DBSCAN(eps=0.1,min_samples=10).fit_predict(X_projected)

##GMM聚类
y_pred=GaussianMixture(n_components=2).fit_predict(X_projected)

##K-means聚类
##y_pred=KMeans(n_clusters=2).fit_predict(X_projected)

##对K-mean的聚类效果进行评分
##score=metrics.calinski_harabasz_score(X_projected,y_pred)
##print(score)

plt.figure(1)
ax = plt.subplot(111, projection='3d')
ax.scatter(X_projected[:,0],X_projected[:,1],X_projected[:,2],c=y)
plt.figure(2)
ax = plt.subplot(111, projection='3d')
ax.scatter(X_projected[:,0],X_projected[:,1],X_projected[:,2],c=y_pred)
plt.show()


