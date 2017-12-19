# 一、pandas简介
## pandas含有使数据分析工作变得更快更简单的高级数据结构和操作工具。
## pandas是基于NumPy构建的，让以NumPy为中心的应用变得更加简单。
from pandas import Series,DataFrame
import pandas as pd

## pandas的两个主要数据结构 Series 和 DataFrame

# 二、Series
## Series 类似一维数组的对象，由一组数据和一组与之相关的数据标签（即索引）组成。

### 1-基本写法
a1 = Series([4,7,-5,3])
### 0    4
### 1    7
### 2   -5
### 3    3
### dtype: int64
### 解释：左边索引，右边数值
### 通过valuse 和index属性获取数组表示形式和索引对象
a1.values                    # array([ 4,  7, -5,  3], dtype=int64)
a1.index                     # RangeIndex(start=0, stop=4, step=1)

### 2-自定义索引标记
a2 = Series([4,7,-5,3],index=['d','b','a','c'])
### d    4
### b    7
### a   -5
### c    3
### dtype: int64
a2.values                     # array([ 4,  7, -5,  3], dtype=int64)
a2.index                      # Index(['d', 'b', 'a', 'c'], dtype='object')

### 3-操作值
a2['a']                       # 获取值  -5
a2['d'] = 6                   # 设置值
a2[['c','a','d']]
### c    3
### a   -5
### d    6
### dtype: int64