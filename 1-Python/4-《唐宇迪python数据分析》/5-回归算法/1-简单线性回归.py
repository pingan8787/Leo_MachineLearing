import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

class LinearRegression():
  def __init__(self):
    self.w = None   # w参数就是上面公式里面的 θ

  def fit(self, X, y):
    # Insert constant ones for bias weights  为偏置权重插入常数
    print(X.shape)
    X = np.insert(X, 0, 1, axis=1)
    print(X.shape)
    X_ = np.linalg.inv(X.T.dot(X))   # X_ 表示处理完后的X值
    self.w = X_.dot(X.T).dot(y)

  def predict(self, X):
    # Insert constant ones for bias weights  为偏置权重插入常数
    X =np.insert(X, 0, 1, axis=1)
    y_pred = X.dot(self.w)
    return y_pred

def mean_squared_error(y_true, y_pred):
  mse = np.mean(np.power(y_true - y_pred,2))
  return mse

def main():
  # Load the diabetes datasets 加载数据
  diabetes = datasets.load_diabetes()

  # Use only one feature 只使用一个特性
  X = diabetes.data[:, np.newaxis, 2]
  print(X.shape)
  # Split the data into training 使用这些数据做测试
  x_train, x_test = X[:-20],X[-20:]
  y_train, y_test = diabetes.target[:-20],diabetes.target[-20:]
  clf = LinearRegression()
  clf.fit(x_train, y_train)
  y_pred = clf.predict(x_test)

  #Print the mean squared error
  print("Mean Square Error:",mean_squared_error(y_test, y_pred))
  
  # Plot the results 
  plt.scatter(x_test[:,0], y_test, color="black")
  plt.plot(x_test[:,0], y_pred, color="blue", linewidth=3)
  plt.show()

main()