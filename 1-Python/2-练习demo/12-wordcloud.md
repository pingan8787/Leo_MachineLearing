### 安装词云库
```shell
pip install wordcloud
```
```python
w = wordcloud.WordCloud()
```

### 简单案例
```python
import wordcloud
c = wordcloud.WordCloud()
c.generate("在坚果Pro2S发布会之后，罗永浩又着实火了一把。不过让他名声大振的不是新机的口碑销量，而是一款堪称黑马级别的即时通讯软件“子弹短信”。伴随着罗永浩本人十分卖力的微博吆喝，以及无数大V在好奇心驱使下的下载宣传，这款软件一度霸占Apple Store总榜第一，网上更是出现了“子弹短信或将取代微信地位”的说法")
c.to_file("a.png")
```

### 参数配置
```python
w = wordcloud.WordCloud(<配置>)

# width,height 图片宽高
w = wordcloud.WordCloud(width=600)

# min_font_size max_font_size 最小字号和最大字号
# font_step 字号间隔
w = wordcloud.WordCloud(min_font_size=16)

# font_path 字体文件路径
w = wordcloud.WordCloud(font_path='msyh.ttc')

# max_words 词云显示的最大单词数量 默认200
# stop_words 排除词列表
w = wordcloud.WordCloud(stop_words=("python"))

# mask 词云形状 默认长方形 需要用imread()函数 图片需要背景白色
from scipy.misc import imread
mk = imread('pic.png')
w = wordcloud.WordCloud(mask = mk)

# background_color 背景色 默认黑色
```

### wordcloud + jieba
```python 
# -*- coding: utf-8 -*-
import jieba
import wordcloud
f = open("wenben.txt",'r',encoding='utf-8')
t = f.read()
ls = jieba.lcut(t)
txt = ' '.join(ls)

## 如果需要更改形状
## from scipy.misc import imread
## mk = imread('pic.png')
## w = wordcloud.WordCloud(mask = mk)

w= wordcloud.WordCloud(width=1000,height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("a1.png")
```