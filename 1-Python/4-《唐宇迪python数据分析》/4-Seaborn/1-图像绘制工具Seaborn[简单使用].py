## Seaborn 是在 Matplotlib 基础上的封装，可以简单绘制出精美图像
## 安装 pip install seaborn

import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# %matplotlib inline

## 1、简单使用
def sinplot(flip=10):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
sinplot()
plt.show()

## 3、Seaborn 自带模版的使用
### Seaborn自带5个模版  darkgrid whitegrid  dark  white  ticks
sns.set_style("whitegrid")
datas = np.random.normal(size=(20, 6))+ np.arange(6)/2
sns.boxplot(data = datas)    # 绘制盒图 数据为 datas
sns.despine()                # 去掉绘图区域上和左边的边框
sns.despine(offset = 10)     #  offset = n  所要绘制的图离横轴的距离 n
sns.despine(left = True)     #  left right top bottom  隐藏对应的轴线
sns.despine(3)               # n 指定第n个子图的风格
plt.show()

## 4、Seaborn 自带布局的使用
### Seaborn自带个布局  paper talk poster notebook
sns.set_context("paper")
## 设置字体大小 线宽等
sns.set_context("paper",font_scale=1.5, rc={"lines.linewidth":2.5})
plt.figure(figsize = (8,6))
sinplot()
plt.show()