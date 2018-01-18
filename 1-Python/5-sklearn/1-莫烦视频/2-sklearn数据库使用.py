# 文档地址：http://sklearn.apachecn.org/cn/0.19.0/modules/classes.html
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

loaded_data = datasets.load_boston()    # 引入需要使用的数据集
data_X = loaded_data.data     # data_x 都是 data
data_y = loaded_data.target   # data_y 都是 target

model = LinearRegression() # 定义模型
model.fit(data_X, data_y)  # 使用模型学习

print(model.predict(data_X[:4,:]))
print(data_y[:4])

## 创造数据点
### (运行下面代码 就要先注释上面代码，保留引用代码)
X,y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=1)
plt.scatter(X,y)
plt.show()