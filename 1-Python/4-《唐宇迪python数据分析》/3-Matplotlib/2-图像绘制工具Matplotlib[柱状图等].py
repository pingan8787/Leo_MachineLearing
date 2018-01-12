# 1、绘制简单柱状图

import pandas as pd
from numpy import arange
import matplotlib.pyplot as plt

reviews = pd.read_csv("fandango_scores.csv")
num_cols = ["RT_user_norm","Metacritic_user_nom","IMDB_norm","Fandango_Ratingvalue","Fandango_Stars"]
norm_reviews = reviews[num_cols]
print (norm_reviews[:1])

bar_heights = norm_reviews.ix[0,num_cols].values      ## 每个柱的高度
bar_positions = arange(5) + 0.75                      ## 每个柱离 0 值的距离
fig,ax= plt.subplots()                                ## 把图拿出来
ax.bar(bar_positions,bar_heights,0.5)                 # ax.bar( 离0点横坐标 , 柱高度 , 柱宽度)
plt.show()