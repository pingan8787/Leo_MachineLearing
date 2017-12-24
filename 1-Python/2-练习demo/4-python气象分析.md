>原文地址：[打开文章](https://www.shiyanlou.com/courses/running#)

# 介绍
学习完基础知识，现在需要一些练习项目，所以网上找了些试试。

# 正文
## 一、实验介绍
本实验将对意大利北部沿海地区的气象数据进行分析与可视化。我们在实验过程中先会运用 `Python` 中 `matplotlib` 库的对数据进行图表化处理，然后调用 `scikit-learn` 库当中的的 `SVM` 库对数据进行回归分析，最终在图表分析的支持下得出我们的结论。  

### 1.1实验知识点
* matplotlib 库画出图像
* scikit-learn 库对数据进行回归分析
* numpy 库对数据进行切片

### 1.2实验环境
* python2.7
* spyder

### 1.4 适合人群
本课程难度为中等，适合具有 `Python` 基础的用户，如果对 `matplotlib` 模块有了解会更快的上手。

## 二、实验步骤
这里省略那些介绍内容，具体查看最上面文章，这里贴代码：

### 2.1实验前准备
```
## 本案例源代码
$ wget http://labfile.oss.aliyuncs.com/courses/780/SourceCode.zip
```

```
## 1.下载所需数据源
$ wget http://labfile.oss.aliyuncs.com/courses/780/WeatherData.zip
## unzip WeatherData.zip

## 2.打开sPyder 并进入目标目录
cd Code
cd WeatherAnalysis
cd WeatherData

## 3.引入数据
df_ferrara = pd.read_csv('ferrara_270615.csv')
df_milano = pd.read_csv('milano_270615.csv')
df_mantova = pd.read_csv('mantova_270615.csv')
df_ravenna = pd.read_csv('ravenna_270615.csv')
df_torino = pd.read_csv('torino_270615.csv')
df_asti = pd.read_csv('asti_270615.csv')
df_bologna = pd.read_csv('bologna_270615.csv')
df_piacenza = pd.read_csv('piacenza_270615.csv')
df_cesena = pd.read_csv('cesena_270615.csv')
df_faenza = pd.read_csv('faenza_270615.csv')

## 3.导入必要的库 
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser

## 4.读取米兰的城市气象数据
df_milano = pd.read_csv('milano_270615.csv')

## 5.取出我们要分析的温度和日期数据
y1 = df_milano['temp']
x1 = df_milano['day']

## 6.把日期数据转换成 datetime 的格式
day_milano = [parser.parse(x) for x in x1]

## 7.调用 subplot 函数, fig 是图像对象，ax 是坐标轴对象
fig, ax = plt.subplots()

## 8.调整x轴坐标刻度，使其旋转70度，方便查看
plt.xticks(rotation=70)

## 9.设定时间的格式
hours = mdates.DateFormatter('%H:%M')

## 10.设定X轴显示的格式
ax.xaxis.set_major_formatter(hours)

## 11.画出图像，day_milano是X轴数据，y1是Y轴数据，‘r’代表的是'red' 红色
ax.plot(day_milano ,y1, 'r')

## 12.显示图像
fig
```
由图可见，气温走势接近正弦曲线，从早上开始气温逐渐升高，最高温出现在下午两点到六点之间，随后气温逐渐下降，在第二天早上六点时达到最低值。  

我们进行数据分析的目的是尝试解释是否能够评估海洋是怎样影响气温的，以及是否能够影响气温趋势，因此我们同时来看几个不同城市的气温趋势。这是检验分析方向是否正确的唯一方式。因此，我们选择三个离海最近以及三个离海最远的城市。    

### 2.2单座城市气温变化图的绘制（这里以米兰为例）
```
## 引入模块
import numpy as np
import pandas as pd
import datetime
```

### 2.3离海最近的三座城市和最远的三座城市气温变化图的绘制
```
##  1.读取数据文件(之前没读取数据的同学，这里一定要读取啦)
df_ravenna = pd.read_csv('ravenna_270615.csv')
df_faenza = pd.read_csv('faenza_270615.csv')
df_cesena = pd.read_csv('cesena_270615.csv')
df_asti = pd.read_csv('asti_270615.csv')
df_torino = pd.read_csv('torino_270615.csv')
df_milano = pd.read_csv('milano_270615.csv')

##  2.读取温度和日期数据
y1 = df_ravenna['temp']
x1 = df_ravenna['day']
y2 = df_faenza['temp']
x2 = df_faenza['day']
y3 = df_cesena['temp']
x3 = df_cesena['day']
y4 = df_milano['temp']
x4 = df_milano['day']
y5 = df_asti['temp']
x5 = df_asti['day']
y6 = df_torino['temp']
x6 = df_torino['day']

##  3.把日期从 string 类型转化为标准的 datetime 类型
day_ravenna = [parser.parse(x) for x in x1]
day_faenza = [parser.parse(x) for x in x2]
day_cesena = [parser.parse(x) for x in x3]
dat_milano = [parser.parse(x) for x in x4]
day_asti = [parser.parse(x) for x in x5]
day_torino = [parser.parse(x) for x in x6]

##  4.调用 subplots() 函数，重新定义 fig, ax 变量
fig, ax = plt.subplots()
plt.xticks(rotation=70)


hours = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hours)

##  5.这里需要画出三根线，所以需要三组参数， 'g'代表'green'
ax.plot(day_ravenna,y1,'r',day_faenza,y2,'r',day_cesena,y3,'r')
ax.plot(day_milano,y4,'g',day_asti,y5,'g',day_torino,y6,'g')
fig
```
上述代码将生成的图表。离海最近的三个城市的气温曲线使用红色，而离海最远的三个城市的曲线使用绿色。  
如图所示，结果看起来不错。离海最近的三个城市的最高气温比离海最远的三个城市低不少，而最低气温看起来差别较小。  

我们可以沿着这个方向做深入研究，收集10个城市的最高温和最低温，用线性图表示气温最值点和离海远近之间的关系。  