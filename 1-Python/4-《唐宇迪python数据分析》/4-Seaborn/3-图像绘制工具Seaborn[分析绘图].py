# 一、单变量分析绘图

import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes= True)
np.random.seed(sum(map(ord,"distributions")))

# 1、绘制直方图
x = np.random.normal(size = 100)
sns.distplot(x,bins = 20,kde=False,fit=stats.gamma)   # x 数据 ，bins 间隔，kde 是否和密度估计，fit 绘制当前变化的指标
plt.show()

# 2、根据均值和协方差绘图
mean,cov = [0,1],[(1, .5),(.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x","y"])

# 3、绘制散点图
### 观测两个变量之间的关系最好用 散点图
sns.jointplot(x="x",y="y", data = df) #  jointplot()绘制散点图 x 第一维度 y 第二维度 data 数据
plt.show()

# 4、绘制hex图  六边形图 适用于数据量大的
x,y = np.random.multivariate_normal(mean, cov, 1000).T
with sns.axes_style("white"):
    sns.jointplot(x=x,y=y,kind="hex",color="k")   # kin指定格式为hex
plt.show()

# 5、绘制四个特征(变量)散点图 展示两两之间的关系
iris = sns.load_dataset("iris")
sns.pairplot(iris)
plt.show()

# 二、回归分析绘图