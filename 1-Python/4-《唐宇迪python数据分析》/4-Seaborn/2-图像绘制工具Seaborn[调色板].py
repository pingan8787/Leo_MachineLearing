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

## 2、圆形画板
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

sns.palplot(sns.color_palette("Paired",10)) # Paired 类型表示颜色成对出现，这里出现5对10个
plt.show()

### 使用skcd颜色来命名颜色
### 用得少 查官网来使用
plt.plot([0, 1],[0, 1],sns.xkcd_rgb["pale_red"], lw = 3)
plt.plot([0, 1],[0, 2],sns.xkcd_rgb["medium_green"], lw = 3)
plt.plot([0, 1],[0, 3],sns.xkcd_rgb["denim_blue"], lw = 3)
plt.show()

## 3、连续画板
sns.palplot(sns.color_palette("Blues"))
plt.show()

sns.palplot(sns.color_palette("BuGn_r"))  # 颜色名加 " _r " 表示翻转渐变色
plt.show()

## 4、cubehelix_palette() 调色板
### 色调线性变换
sns.palplot(sns.color_palette("cubehelix", 8))
plt.show()

sns.palplot(sns.cubehelix_palette(8, start=.5, rot=-0.75))  # start rot 指定颜色区间
plt.show()

sns.palplot(sns.cubehelix_palette(8, start=.75, rot=-.150))
plt.show()

## 5、light_palette() 和 dark_palette 调用定制连续调色板
sns.palplot(sns.light_palette("green"))
plt.show()

sns.palplot(sns.light_palette("purple"))
plt.show()

sns.palplot(sns.light_palette("navy", reverse=True))  # reverse 倒序排序颜色
plt.show()

x, y = np.random.multivariate_normal([0, 0],[[1,-.5],[-.5,1]],size=300).T
pal = sns.dark_palette("green",as_cmap=True)
sns.kdeplot(x,y,cmap=pal)
plt.show()

sns.palplot(sns.light_palette((210,90,60)),input="husl") # input 指定颜色空间 基本不用
plt.show()