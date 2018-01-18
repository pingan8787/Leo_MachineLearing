from sklearn import preprocessing
import numpy as np
from sklearn.cross_validation import train_test_split  # 这个模块是将test集和train集数据分开
from sklearn.datasets.samples_generator import make_classification    # 用于生成classification数据
from sklearn.svm import SVC   # 处理数据当做model
import matplotlib.pyplot as plt  # 可视化数据

# a = np.array([[100,2.7,3.6],
#               [-100,5,-5],
#               [120,20,40]],dtype=np.float64)
# print(a)
# 处理数据 normalization 标准化 使得机器学习处理数据更方便
# 介绍 https://github.com/pingan8787/Leo_MachineLearing/blob/master/1-Python/5-sklearn/images/1_1_normalization.png?raw=true
# print(preprocessing.scale(a))


# 生成data 

X,y = make_classification(n_samples=300, n_features=2,n_redundant=0,n_informative=2,random_state=22,n_clusters_per_class=1,scale=100)
# plt.scatter(X[:,0],X[:,1],c=y)
# plt.show()

X = preprocessing.scale(X)  # 压缩数据取值范围到0-1  featrue_range 默认值 (0,1)
# X = preprocessing.scale(X,featrue_range=(0,1))

# 进行机器学习步骤
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = .3)
clf = SVC()
clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))