# 1、简单折线图绘制

## UNRATE.csv 数据为美国统计的未就业人口占比

import pandas as pd
unrate = pd.read_csv("./unrate.csv")
unrate['DATE'] = pd.to_datetime(unrate['DATE'])  # 类型转换 to_datetime()
print(unrate.head(12))

## 设置中文乱码问题
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

import matplotlib.pyplot as plt
first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'], first_twelve['VALUE']) # plt.plot( x轴数据, y轴数据)
plt.xticks(rotation = 45)   # 变换坐标角度
plt.xlabel("月份")         # x轴标题
plt.ylabel("失业率")       # y轴标题
plt.title("美国人口失业分布")     # 图表标题

plt.show()       # 显示图像


# 2、子图操作
## 使用 fig.add_subplot(a,b,c)  a:行数  b:列数  c:排序位置
import matplotlib.pyplot as plt
fig = plt.figure()   # 定义绘图区域
ax1 = fig.add_subplot(4,3,1)
ax2 = fig.add_subplot(4,3,2)
ax3 = fig.add_subplot(4,3,6)
plt.show()

import numpy as np
fig = plt.figure(figsize = (8,6))   # figure的figsize=(w,h) 表示绘图区域的宽高
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(np.random.randint(1,5,5), np.arange(5))
ax2.plot(np.arange(10)*3, np.arange(10))
plt.show()