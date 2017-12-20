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

### 4-Series看成字典
'b' in a2                     # True
'e' in a2                     # False

### 5-通过python字典创建Series
a3 = {'a':12,'b':13,'c':14,'d':15}   # {'a': 12, 'b': 13, 'c': 14, 'd': 15}
a4 = Series(a3)
### a    12
### b    13
### c    14
### d    15
### dtype: int64
### 如果传入这样一个字典，就会这种情况
a5 = {'f','a','b','c'}
a6 = Series(a3,index=a5)
### f     NaN
### c    14.0
### b    13.0
### a    12.0
### dtype: float64

### 6-含有运算和判断
a7 = Series({'d':6,'c':3,'a':-2,'b':6})
### a   -2
### b    6
### c    3
### d    6
### dtype: int64
a7[a7 > 0]
### b    6
### c    3
### d    6
### dtype: int64
a7 * 2
### a    -4
### b    12
### c     6
### d    12
### dtype: int64
np.exp(a7)
### a      0.135335
### b    403.428793
### c     20.085537
### d    403.428793
### dtype: float64


# 三、DataFrame
## DataFrame是一个表格型数据结构，含有一组有序的列，每列可以是不同类型的值。
## 可以看成由Series组成的字典。
d1 = {'state':['a','b','c','d','e'],
'year':[2011,2012,2013,2014,2015],
'pop':[1.1,1.5,1.9,2.1,2.3]}
d2 = DataFrame(d1)
###    pop state  year
### 0  1.1     a  2011
### 1  1.5     b  2012
### 2  1.9     c  2013
### 3  2.1     d  2014
### 4  2.3     e  2015

### 1.指定列来排序
d3 = DataFrame(d1,columns=['year','state','pop'])
###    year state  pop
### 0  2011     a  1.1
### 1  2012     b  1.5
### 2  2013     c  1.9
### 3  2014     d  2.1
### 4  2015     e  2.3

### 2.获取列名
d3.columns       #  Index(['year', 'state', 'pop'], dtype='object')

### 3.通过类似字典标记或属性获取DataFrame的列为一个Series
d3['year']      # 或者 d3.year
### 0    2011
### 1    2012
### 2    2013
### 3    2014
### 4    2015
### Name: year, dtype: int64

### 4.给一列赋值
d3['state'] = 'haha'
###    year state  pop
### 0  2011  haha  1.1
### 1  2012  haha  1.5
### 2  2013  haha  1.9
### 3  2014  haha  2.1
### 4  2015  haha  2.3

### 5.嵌套字典的数据格式
### 外层字典的键作为列
### 内层键作为行索引
d3 = {
    'title1':{2001:2.3,2002:2.9},
    'title2':{2000:2.1,2005:2.5}
}
d4 = DataFrame(d3)
###       title1  title2
### 2000     NaN     2.1
### 2001     2.3     NaN
### 2002     2.9     NaN
### 2005     NaN     2.5
### 也可以对结果转置
d4.T
###         2000  2001  2002  2005
### title1   NaN   2.3   2.9   NaN
### title2   2.1   NaN   NaN   2.5

### 6.设置name属性
### 如果设置了DataFrame的index和columns的name属性，那么这些信息会直接被显示出来：
d4.index.name='header1';d4.columns.name='header2'
### header2  title1  title2
### header1
### 2000        NaN     2.1
### 2001        2.3     NaN
### 2002        2.9     NaN
### 2005        NaN     2.5

# 四、索引对象
### pandas的索引对象负责管理轴标签和其他元数据（比如轴名称等）。
### 构建Series或DataFrame时，所用到的任何数组或其他序列的标签都会被转换成一个Index：
e1 = Series(range(3),index=['a','b','c'])
### a    0
### b    1
### c    2
### dtype: int32
e2 = e1.index          # Index(['a', 'b', 'c'], dtype='object')
e2[1:]                 # Index(['b', 'c'], dtype='object')
e2[1] = 'd'            # 直接报错 !!!!Index对象是不可修改的
### index的属性方法：append/diff/intersection/union/isin/delete/drop/insert/is_monotonic/is_unique/unique

### 更多使用方法，查看书本