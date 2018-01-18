## sklearn提供很多种数据库方便学习机器学习。
## 这份代码是讲sklearn通用学习模式

import numpy as np
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data 
iris_y = iris.target

# print(iris_X[:2,:])
# print(iris_y)

## 将数据分成两类 train训练集 和 test测试集
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)   
# test_size 测试集(X_train,y_train)数据占30%  

# print(y_train)

knn = KNeighborsClassifier()  # 定义sklearn使用哪个模块的方式
knn.fit(X_train, y_train)     # 最重要  将数据放进去 自动完成train训练
print(knn.predict(X_test))    # 这里的knn是已经训练完成的数据
print(y_test)