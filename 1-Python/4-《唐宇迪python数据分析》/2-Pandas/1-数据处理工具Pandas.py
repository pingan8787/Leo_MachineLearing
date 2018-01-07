import pandas as pd

# 1、读取文件数据
pk10 = pd.read_csv("../pk10.txt")
print(pk10.dtypes)         # 当前数据中包含的所有数据类型
print(help(pd.read_csv))   # 返回这个方法怎么用

pk10.head()                 # 显示表格 (默认前五条)  pk10.head(n) 默认前n条
pk10.tail()                 # 显示表格 (默认后五条)  pk10.head(n) 默认后n条