# pandas对象中的数据可以使用内置的方式进行合并：
import numpy as np
from pandas import Series,DataFrame
import pandas as pd


## 1、pandas.merge 根据一个或多个键 将不同DataFrame中的行连接起来。
## 数据库风格的DataFrame合并     还可以查看：https://www.cnblogs.com/HixiaoDi/p/7739863.html
### 数据集的合并（merge）或连接（join）运算是通过一个或多个键将行连接在一起。
a1 = DataFrame({'key':['b','b','a','c','a','a','b'],'d1':range(7)})
a2 = DataFrame({'key':['a','b','c'],'d2':range(3)})
### 这是中多对一的合并，a1有多个标记为a和b的行，而a2的key列每个值则对应一行，使用merge即：
a3 = pd.merge(a1,a2)
###    d1 key  d2
### 0   0   b   1
### 1   1   b   1
### 2   6   b   1
### 3   2   a   0
### 4   4   a   0
### 5   5   a   0
### 6   3   c   2
### 若没有指定用哪个列进行连接，则merge将重叠列的列名作为键，也可以显式指定：
a4 = pd.merge(a1,a2,on="key")
###    d1 key  d2
### 0   0   b   1
### 1   1   b   1
### 2   6   b   1
### 3   2   a   0
### 4   4   a   0
### 5   5   a   0
### 6   3   c   2

## 若两个对象的列名不同，也可以分别进行指定
a5 = DataFrame({'lkey':['b','b','a','c','a','a','b'],'d1':range(7)})
a6 = DataFrame({'rkey':['a','b','c'],'d2':range(3)})
a7 = pd.merge(a5,a6,left_on="lkey",right_on="rkey")
###    d1 lkey  d2 rkey
### 0   0    b   1    b
### 1   1    b   1    b
### 2   6    b   1    b
### 3   2    a   0    a
### 4   4    a   0    a
### 5   5    a   0    a
### 6   3    c   2    c

## 由于merge默认使用'inner'连接，使得'c'和'd'相关数据消失，只显示结果中的键的交集。
## 另外还有'left','right','outer'方式
a8 = pd.merge(a1,a2,how="outer")
###    d1 key  d2
### 0   0   b   1
### 1   1   b   1
### 2   6   b   1
### 3   2   a   0
### 4   4   a   0
### 5   5   a   0
### 6   3   c   2

## 多对多的合并
a9 = DataFrame({'key':['b','b','a','c','a','b'],'d1':range(6)})
a10 = DataFrame({'key':['a','b','a','b','d'],'d1':range(5)})
a11 = pd.merge(a9,a10,on="key",how="left")
###     d1_x key  d1_y
### 0      0   b   1.0
### 1      0   b   3.0
### 2      1   b   1.0
### 3      1   b   3.0
### 4      2   a   0.0
### 5      2   a   2.0
### 6      3   c   NaN
### 7      4   a   0.0
### 8      4   a   2.0
### 9      5   b   1.0
### 10     5   b   3.0


## 2、pandas.concat 可以沿着一条轴将多个对象堆叠到一起。
## 3、实例方法combine_first可以将重复数据编接到一起，用一个对象中的键填充对象中的缺失值。
