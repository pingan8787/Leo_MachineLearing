## Series 相当于DataFrame的某一行或某一列
## Series 是 ndarray 类型
import pandas as pd
import numpy as np

titanic = pd.read_csv('../train.csv')
fares = titanic["Fare"]
Embarked = titanic['Embarked']
print( type(fares) )    # <class 'pandas.core.series.Series'>
print( fares[0:5] )

from pandas import Series

a1 = fares.values
print( type(a1) )       # <class 'numpy.ndarray'>

## 创建新Series
a2 = Series(a1, index = Embarked)
a3 =  a2[['Q','C']]     # 筛选Q 和 C

## 排序
original_index = a3.index.tolist()
a4 = sorted(original_index)
a5 = a3.reindex(a4)
b1 = a2.sort_index()
b2 = a2.sort_values()

## 相加
import numpy as np
print(np.add(a2,a2))
print(np.sin(a2))
print(np.max(a2))

## 条件判断
a2 > 10
a2_than_10 = a2[a2 > 10]
c1 = a2 > 10
c2 = a2 < 20
c3 = a2[c1 & c2]

## 设置指定索引
titanic = pd.read_csv('../train.csv')
titanic_name = titanic.set_index('Name',drop = False)  # 指定 Name 列作为索引
print( titanic_name["Montvila, Rev. Juozas":"Dooley, Mr. Patrick"] )  # 用新的索引 查找
print( titanic_name.loc["Montvila, Rev. Juozas":"Dooley, Mr. Patrick"] )

