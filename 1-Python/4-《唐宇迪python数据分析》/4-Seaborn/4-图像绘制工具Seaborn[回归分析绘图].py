import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes= True)
np.random.seed(sum(map(ord,"regression")))

tips = sns.load_dataset("tips")
tips.head()

## 绘制回归关系方式有2种
# 1、绘图方式1 regplot() 推荐
sns.regplot(x = "total_bill",y="tip",data=tips) # x x轴数据 y y轴数据 data 当前dataFrame
plt.show()

# 2、绘图方式2 lmplot()
sns.lmplot(x = "total_bill",y="tip",data=tips) # x x轴数据 y y轴数据 data 当前dataFrame
plt.show()

# 3、添加抖动值 x_jitter
sns.regplot(x = "size",y="tip",data=tips ,x_jitter=.05)  # x_jitter 使得原始值随机增加发生浮动
plt.show()