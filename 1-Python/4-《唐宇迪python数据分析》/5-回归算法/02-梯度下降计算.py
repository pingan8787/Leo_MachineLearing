# 一、绘制图像

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pga = pd.read_csv("../data/pga.csv")

# 初始化数据
pga.distance = (pga.distance - pga.distance.mean()) / pga.distance.std()
pga.accuracy = (pga.accuracy - pga.accuracy.mean()) / pga.accuracy.std()
# # 绘图
# plt.scatter(pga.distance, pga.accuracy)
# plt.xlabel("初始化距离")
# plt.ylabel("初始化准确值")
# plt.show()


# # 二、计算梯度下降
# ## 1、非梯度下降法
# ## 定义目标函数(损失函数)
# def cost(theta0, theta, x, y):
#     J = 0
#     m = len(x)
#     for i in range(m):
#         h = theta * x[i] + theta0
#         J += (h - y[i])**2
#     J /= (2*m)
#     return J
# print(cost(0, 1, pga.distance, pga.accuracy))

# theta0 = 100
# thetals = np.linspace(-3, 2, 100)
# costs = []
# for thetal in thetals:
#     costs.append(cost(theta0, thetal, pga.distance, pga.accuracy))
# plt.plot(thetals, costs)
# plt.show()    


## 2、梯度下降法
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X,Y = np.meshgrid(x, y)
Z = X**2 + Y **2
fig = plt.figure()
ax = fig.gca(projection="3d")
ax.plot_surface(X=X,Y=Y,Z=Z)
plt.show()

theta0s = np.linspace(-2, 2, 100)
theta1s = np.linspace(-2, 2, 100)
COST = np.empty(shape = (100, 100))
TOS, T1S = np.meshgrid(theta0s, theta1s)
for i in range(100):
    for j in range(100):
        COST[i, j] = cost(TOS[0, i], T1S[j, 0], pga.distance, pga.accuracy)
fig2 = plt.figure()
ax = fig2.gca(projection="3d")
ax.plot_surface(X = TOS, Y=T1S, Z=COST)
plt.show()