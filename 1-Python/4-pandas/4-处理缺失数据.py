import numpy as np
from pandas import Series,DataFrame
import pandas as pd

## 确实数据在大部分数据分析应用中都很常见。pandas的设计目标之一就是让缺失数据的处理任务尽量轻松。
## pandas使用浮点值NaN表示浮点与非浮点数组中的缺失数据，它知识一个便于被检测出来的标记而已。
a1 = Series(['a','b',np.nan,'d'])
a1.isnull()

### python内置的None值也会被当做NA处理：
a1[0] = None
a1.isnull()
### NA处理方法，查看书文《利用python进行数据分析》P149

## 1.过滤缺失数据
### 对于Series使用dropna返回一个仅含非空数据和所引致的Series:
from numpy import nan as NA
b1 = Series([1,NA,3.5,NA,7])
b1.dropna()  # 或者使用 b1[b1.notnull()]
### 0    1.0
### 2    3.5
### 4    7.0
### dtype: float64

### 对于DataFrame drop默认丢弃任何含有缺失值的行：
b2 = DataFrame([[1.,2.,3.],[1.,NA,NA],[NA,NA,NA],[NA,6,7]])
b3 = b2.dropna()
###      0    1    2
### 0  1.0  2.0  3.0

### 传入 how='all' 则只丢弃全部是NA的行
b2.dropna(how='all')
###      0    1    2
### 0  1.0  2.0  3.0
### 1  1.0  NaN  NaN
### 3  NaN  6.0  7.0
### 传入 how='all'和axis=1 则只丢弃全部是NA的列
b2.dropna(how='all',axis=1)
###      0    1    2
### 0  1.0  2.0  3.0
### 1  1.0  NaN  NaN
### 2  NaN  NaN  NaN
### 3  NaN  6.0  7.0