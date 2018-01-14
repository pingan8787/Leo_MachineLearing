## 调色板 颜色很重要
## color_palette() 能传入任何 Matplotlib 所支持的颜色
## color_palette() 不写参数则默认颜色
## set_palette()设置所有图的颜色

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc = {"figure.figsize": (6,6)})

## 1、分类色板
## 6个默认循环颜色主题：deep, muted, pastel, bright, datk, colorblind
current_palette = sns.color_palette()    # 没有传入颜色 则使用默认
sns.palplot(current_palette)
plt.show()

## 3、圆形画板
### 即在一个圆形的颜色空间中均匀间隔的分布颜色 最常用的是hls的颜色空间，这是RGB值的一个简单转换
sns.palplot(sns.color_palette("hls", 8))  # 均匀平分成8份
plt.show()

data = np.random.normal(size=(20, 8)) + np.arange(8) / 2
sns.boxplot(data = data, palette=sns.color_palette("hls",8))
plt.show()

### hls_palette() 函数控制颜色的亮度和饱和度
### l - 亮度 lightness
### s - 饱和度 saturation
sns.palplot(sns.hls_palette(8, l=.3, s=.8))  # hls_palette( 颜色数量，亮度，饱和度)
plt.show()

sns.palplot(sns.color_palette("Paired",10))
plt.show()