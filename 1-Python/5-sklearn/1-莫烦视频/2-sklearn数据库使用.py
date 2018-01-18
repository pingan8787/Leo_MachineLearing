# 文档地址：http://sklearn.apachecn.org/cn/0.19.0/modules/classes.html
from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()    # 引入需要使用的数据集
data_X = loaded_data.data     # data_x 都是 data
data_y = loaded_data.target   # data_y 都是 target

model = LinearRegression() # 定义模型
model.fit(data_X, data_y)  # 使用模型学习