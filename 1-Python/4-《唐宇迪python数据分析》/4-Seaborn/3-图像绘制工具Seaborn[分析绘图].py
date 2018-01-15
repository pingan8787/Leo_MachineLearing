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

# ================================ #

# 二、多变量分析绘图

import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="shitefrid",color_codes=True)

np.random.seed(sum(map(ord,"categorical")))
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

# 1、绘制 stripplot 图
sns.stripplot(x="day", y="total_bill",data=tips)   # 这样绘图 点太集中 不好分析
sns.stripplot(x="day", y="total_bill",data=tips, jitter=True)   # 添加jitter 更适合分析
plt.show()

# 2、绘制 swarmplot 图
sns.swarmplot(x="day", y="total_bill",data=tips, hue="sex")  # hue="sex" 绘制图例
sns.swarmplot(x="total_bill", y="day",data=tips, hue="time")  # hue="time" 绘制图例
plt.show()

# 3、绘制 boxplot 图（盒图）
## IQR即统计学概念四分位距，第一/四分位与第三/四分位之间的距离 如100个样本 则去25 和 75 之间距离
## N = 1.5IQR 如果一个值>Q3+N 或 < Q1-N,则为离群点
sns.boxplot(x="day", y="total_bill", hue="time", data=tips)
plt.show()
## 图中 单独的菱形点为离群点 上下横线代表最大最小值

# 4、绘制 violinplot 图 （小提琴图）
sns.violinplot(x="total_bill", y="day", hue="time", data=tips)
plt.show()

sns.violinplot(x="day", y="total_bill", hue="sex", data=tips,split=True)
plt.show()

# 5、多种图组合
sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
sns.swarmplot(x="day", y="total_bill",data=tips, color="w", alpha=.5)
plt.show()

# 6、绘制 barplot 柱形图
sns.barplot(x="sex", y="survived", hue="class",data=titanic)
plt.show()

# 7、绘制 pointplot 点图
## 更好的描述变化差异
sns.pointplot(x = "sex", y = "survived", hue="class", data=titanic)
plt.show()