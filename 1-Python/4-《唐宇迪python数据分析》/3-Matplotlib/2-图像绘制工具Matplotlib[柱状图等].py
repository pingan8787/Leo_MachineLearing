# 0、通用代码
import pandas as pd
from numpy import arange
import matplotlib.pyplot as plt

reviews = pd.read_csv("fandango_scores.csv")
num_cols = ["RT_user_norm","Metacritic_user_nom","IMDB_norm","Fandango_Ratingvalue","Fandango_Stars"]
norm_reviews = reviews[num_cols]
print (norm_reviews[:1])

## 设置中文乱码问题
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 1、绘制简单柱状图
bar_heights = norm_reviews.ix[0,num_cols].values      ## 每个柱的高度
bar_positions = arange(5) + 0.75                      ## 每个柱离 0 值的距离
fig,ax= plt.subplots()                                ## 把图拿出来
ax.bar(bar_positions,bar_heights,0.5)                 # ax.bar( 离0点横坐标 , 柱高度 , 柱宽度)
plt.show()

# 2、绘制带有title和label的柱状图
bar_heights = norm_reviews.ix[0,num_cols].values      ## 每个柱的高度
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
fig,ax = plt.subplots()

ax.bar(bar_positions, bar_heights, 0.5)               # ax.bar() 绘制纵向柱状图
ax.set_xticks(tick_positions)                         # 设置 x 轴刻度值
ax.set_xticklabels(num_cols,rotation=45)              # 设置 x 轴刻度值的旋转角度
ax.set_xlabel("Rating Source")                     # 设置 x 轴名称
ax.set_ylabel("Average Rating")                    # 设置 y 轴名称
ax.set_title("这是标题")                             # 设置 图表 标题
plt.show()

# 3、绘制横向柱状图
bar_heights = norm_reviews.ix[0,num_cols].values      ## 每个柱的高度
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
fig,ax = plt.subplots()

ax.barh(bar_positions, bar_heights, 0.5)               # ax.bar() 绘制横向柱状图
ax.set_xticks(tick_positions)                         # 设置 x 轴刻度值
ax.set_xticklabels(num_cols,rotation=45)              # 设置 x 轴刻度值的旋转角度
ax.set_xlabel("Rating Source")                     # 设置 x 轴名称
ax.set_ylabel("Average Rating")                    # 设置 y 轴名称
ax.set_title("这是标题")                             # 设置 图表 标题
plt.show()

# 4、绘制简单散点图
fig,ax = plt.subplots()
ax.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["RT_user_norm"])
ax.set_xlabel("Fandango")
ax.set_ylabel("Rotten Tomatoes")
plt.show()