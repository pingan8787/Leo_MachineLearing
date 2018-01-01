import numpy as np
from pandas import Series,DataFrame
import pandas as pd

## pandas对象拥有一组常用的数学和统计方法，大部分属于约简和汇总统计。
## 用于从Series中提取单个值（如sum或mean），或从DataFrame的行或列提取一个Series。

a1 = DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
###     one  two
### a  1.40  NaN
### b  7.10 -4.5
### c   NaN  NaN
### d  0.75 -1.3
a1.sum()      # sum()方法返回一个含有列小计的Series
### one    9.25
### two   -5.80
### dtype: float64

## 传入axis=1会按 `行` 进行求和运算,NA值会自动被排除，可以通过skipna选项禁用该功能
a1.sum(axis = 1)
# a1.sum(axis = 1 ,skipna = False)
### a    1.40
### b    2.60
### c    0.00
### d   -0.55
### dtype: float64

# 常用约简方法选项：
#-------------------------------------------------#
#     axis  --    约简的轴，DataFrame的行用0,列用1  #
#    skipna --    排除缺失值，默认True              #
#     level --    如果轴是层次化索引，则根据level分组#
#-------------------------------------------------#

# 有些是间接统计（如达到最大值或最小值的索引）
a1.idxmax()
### one    b
### two    d
### dtype: object

# 有些是累计型
a1.cumsum()
###     one  two
### a  1.40  NaN
### b  8.50 -4.5
### c   NaN  NaN
### d  9.25 -5.8

# 还有的既不是约简型也不是累计型，如desribe,用于一次性产生多个汇总统计：
a1.describe()
###             one       two
### count  3.000000  2.000000
### mean   3.083333 -2.900000
### std    3.493685  2.262742
### min    0.750000 -4.500000
### 25%    1.075000 -3.700000
### 50%    1.400000 -2.900000
### 75%    4.250000 -2.100000
### max    7.100000 -1.300000

# 对于非数值类型数据,describe会产生另外一种汇总统计：
a2 = Series(['a','b','b','c'] * 4)
a2.describe()
### count     16
### unique     3
### top        b
### freq       8
### dtype: object
## 更多描述和汇总统计方法，查看《利用Python进行数据分析》P144

##########################################

# 唯一值、值计数以及成员资格
## 从一维Series的值中抽取信息
b1 = Series(['c','a','d','a','b','b','c','c'])
## unique获取Series中唯一值数组
b2 = b1.unique()
### array(['c', 'a', 'd', 'b'], dtype=object)

## 返回的唯一值是未排序的，可以对结果再次排序(uniques.sort())。
## value_counts()用于计算一个Series中各值出现的频率,默认按降序排列
b1.value_counts()
### c    3
### a    2
### b    2
### d    1
### dtype: int64

## value_counts()还是一个顶级pandas方法，可用于任何数组或序列：
pd.value_counts(b1.values,sort=False)
### b    2
### d    1
### a    2
### c    3
### dtype: int64

# 还有isin 判断矢量化集合的成员资格，可用于选取Series中或DataFrame列中的数据的子集：
## 表示Series各值是否包含于传入的值序列中，返回布尔值
c1 = Series(['c','a','d','a','b','b','c','c'])
c2 = c1.isin(['b','c'])
c2[c1]