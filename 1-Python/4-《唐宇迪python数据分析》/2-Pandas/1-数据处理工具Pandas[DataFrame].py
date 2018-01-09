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

# 3、算术运算  对指定列的所有数据
print( pk10['section'] + 100 )
print( pk10['section'] - 100 )
print( pk10['section'] * 100 )
print( pk10['section'] / 100 )
## 两个相同列的算术运算 维度一样就会找对应位置的值计算
print( pk10['section'] + pk10['date'] )
print( pk10['section'] - pk10['date'] )
print( pk10['section'] * pk10['date'] )
print( pk10['section'] / pk10['date'] )
## 添加一个新的列
new_list = pk10['section'] / 100
pk10['newlist'] = new_list

# 4、常用函数
## 查找某一列最大值
print( pk10['section'].max() )
print( pk10['section'] / pk10['section'].max() )

## 排序
pk10.sort_values('section',inplace=True)    # inplace：表示是否在原DataFrame里面排序，false则是在新DataFrame里面排序
pk10.sort_vlaues('section',inplace=True,ascending=False)   #  ascending表示排序方法，排序默认升序，值为False为降序