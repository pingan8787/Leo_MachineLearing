# pandas对象中的数据可以使用内置的方式进行合并：
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
## 1、pandas.merge 根据一个或多个键 将不同DataFrame中的行连接起来。
## 数据库风格的DataFrame合并
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


## 2、pandas.concat 可以沿着一条轴将多个对象堆叠到一起。
## 3、实例方法combine_first可以将重复数据编接到一起，用一个对象中的键填充对象中的缺失值。
