# 笔记内容根据《利用Python进行数据分析》整理。
# 一、重新索引

## 1.reindex，重新索引
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
###    haha  hehe  heihei
### a   0.0   1.0     2.0
### b   NaN   NaN     NaN
### c   3.0   4.0     5.0
### d   6.0   7.0     8.0
## 使用columns关键字重新索引列
a7 = a5.reindex(columns=['heihei','hehe','haha'])
###    heihei  hehe  haha
### a       2     1     0
### c       5     4     3
### d       8     7     6
## 同时对行和列重新索引，而插值只能按行应用（即轴0）
a8 = a5.reindex(index=['a','b','c','d'],columns=['heihei','hehe','haha'],method='ffill')
###    heihei  hehe  haha
### a       2     1     0
### b       2     1     0
### c       5     4     3
### d       8     7     6

## reindex的参数有index/method/fill_value/limit/level/copy 具体查看书本

## 2.loc，重新索引
import numpy as np
b1 = DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['haha','hehe','heihei'])
b2 = b1.loc[['a','b','c','d'],['heihei','hehe','haha']]
# b2 = b1.ix[['a','b','c','d'],['heihei','hehe','haha']]
## .ix方法弃用， 改用.loc或.iloc
## 文档http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
###    heihei  hehe  haha
### a     2.0   1.0   0.0
### b     NaN   NaN   NaN
### c     5.0   4.0   3.0
### d     8.0   7.0   6.0

## 3.丢弃指定轴上的项
### 使用drop方法，并返回删除后的新对象
### 1)对于Series
c1 = Series(np.arange(5.),index=['a','b','c','d','e'])
c2 = c1.drop(['b','c','d'])
### a    0.0
### e    4.0
### dtype: float64

### 2)对于DataFrame
c3 = DataFrame(np.arange(16).reshape((4,4)),index=['aa','bb','cc','dd'],columns=['a1','b1','c1','d1'])
c4 = c3.drop(['aa','cc','dd'])
###     a1  b1  c1  d1
### bb   4   5   6   7