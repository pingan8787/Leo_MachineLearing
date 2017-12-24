# 笔记内容根据《利用Python进行数据分析》整理。
# 一、重新索引
## pandas对象的一个重要方法是reindex，作用是创建一个适应新索引的新对象
a1 = Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
a2 = a1.reindex(['a','b','c','d','e'])
### a   -5.3
### b    7.2
### c    3.6
### d    4.5
### e    NaN
### dtype: float64
## fill_value属性：在重排时代替值为NaN的值
a3 = a1.reindex(['a','b','c','d','e'],fill_value=0)

## method选项使用ffill，实现前向值填充
a4 = Series(['bule','purple','yellow'],index=[0,2,4])
### 0      bule
### 2    perple
### 4    yellow
### dtype: object
a4.reindex(range(6),method='ffill')
### 0      bule
### 1      bule
### 2    purple
### 3    purple
### 4    yellow
### 5    yellow
### dtype: object
## method选项：
## ffill, bfill　 向前填充/向后填充
## pad, backfill　向前搬运，向后搬运

## 对于DataFrame,reindex可以修改(行)索引、列、或者两个都修改。传入一个序列，则会重新索引行：
import numpy as np
a5 = DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['haha','hehe','heihei'])
a6 = a5.reindex(['a','b','c','d'])
## 使用columns关键字重新索引列
a7 = a5.reindex(columns=['heihei','hehe','haha'])

