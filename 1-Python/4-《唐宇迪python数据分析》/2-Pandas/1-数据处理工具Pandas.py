import pandas as pd

# 1、读取文件数据
pk10 = pd.read_csv("../pk10.csv")
print(pk10.dtypes)         # 当前数据中包含的所有数据类型
print(help(pd.read_csv))   # 返回这个方法怎么用

pk10.head()                 # 显示表格 (默认前五条)  pk10.head(n) 默认前n条
pk10.tail()                 # 显示表格 (默认后五条)  pk10.head(n) 默认后n条

# 2、索引和计算 取数据
print( pk10.loc[0] )       # pandas中索引不是直接 pk10[0] 获取，而是通过 .loc[0] 来获取
print( pk10.loc[3:6] )     # 切片取值
arr1 = [3,6,9]              # 需要先组成 list 结构
print( pk10.loc[arr1] )    # 获取指定的多个索引的值

## 获取指定列的数据
print( pk10['date'] )     # 获取单个列
arr2 = ['date','section']# 需要先组成 list 结构
print( pk10[arr2] )        # 获取多个列

## 获取所有列名
col_names = pk10.columns.tolist()