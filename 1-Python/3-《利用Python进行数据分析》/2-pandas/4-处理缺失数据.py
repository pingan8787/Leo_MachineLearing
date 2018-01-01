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


## 2.填充缺失数据
### 常常使用fillna方法，将缺失值替换为一个常数值
c1 = DataFrame(np.random.randn(7,3))
c1.iloc[:4,1] = NA
c1.iloc[:2,2] = NA
c1.fillna(0)
###           0         1         2
### 0 -0.547448  0.000000  0.000000
### 1  0.453079  0.000000  0.000000
### 2 -0.953695  0.000000  1.030625
### 3  1.195861  0.000000 -0.435647
### 4 -0.350453  0.000000 -1.056800
### 5 -1.167823 -0.682913  0.363704
### 6  0.225280 -1.414945  0.687797

### 若通过一个字典调用fillna，就可以实现对不同的列填充不同的值
c1.fillna({1:0.5,3:-1})
###           0         1         2
### 0 -0.547448  0.500000       NaN
### 1  0.453079  0.500000       NaN
### 2 -0.953695  0.500000  1.030625
### 3  1.195861  0.500000 -0.435647
### 4 -0.350453  0.500000 -1.056800
### 5 -1.167823 -0.682913  0.363704
### 6  0.225280 -1.414945  0.687797

### 对reindex有效的那些插值方法也可以用于fillna:
c2 = DataFrame(np.random.randn(6,3))
c2.iloc[2:,1] = NA
c2.iloc[4:,2] = NA
c2.fillna(method='ffill')
c2.fillna(method='ffill',limit=2)
### 转变利用fillna实现很多功能。如传入Series的平均值或中位数
d1 = Series([1.,NA,3.5,NA,7])
d1.fillna(d1.mean())



### fillna函数的参数，查看书文《利用python进行数据分析》P152