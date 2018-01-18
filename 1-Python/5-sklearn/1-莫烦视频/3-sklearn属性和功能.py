# 文档地址：http://sklearn.apachecn.org/cn/0.19.0/modules/classes.html
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

loaded_data = datasets.load_boston()    # 引入需要使用的数据集
data_X = loaded_data.data     # data_x 都是 data
data_y = loaded_data.target   # data_y 都是 target

model = LinearRegression() # 定义模型
model.fit(data_X, data_y)  # 使用模型学习

###  ↑↑↑上节内容
###  ↓↓↓本节内容 model的属性和功能
## 例如公式 y = 0.1x + 0.3  
# model.conf_ => 0.1 (类似斜率)   
# model.intercept_ => 0.3 (类似和x轴的交点)
print(model.coef_)
print(model.intercept_)
print(model.get_params())  # 返回之前定义的参数  
print(model.score(data_X, data_y))  # 使用R^2 coefficient of determination 对model学习进行打分，用data_X做预测 和 data_y进行对比
## 参数介绍 http://sklearn.apachecn.org/cn/0.19.0/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression