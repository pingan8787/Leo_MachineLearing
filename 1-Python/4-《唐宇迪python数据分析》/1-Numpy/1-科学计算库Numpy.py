import numpy as np

# 1、读取文件数据
pk10 = np.genfromtxt("../pk10.txt",delimiter="	",dtype="str")  # 读取文件数据，并且指定“	”为分隔符
print(type(pk10))
print(pk10)
print(help(np.genfromtxt))   # 查看函数的帮助文档
'''
<class 'numpy.ndarray'>
[['2017-12-15' '656198' '5,1,8,2,9,3,10,4,7,6']
 ['2017-12-15' '656197' '5,9,10,4,2,7,3,6,8,1']
 ['2017-12-15' '656196' '4,9,7,2,3,6,1,5,10,8']
 ...,
 ['2012-01-01' '274575' '3,7,10,4,8,6,9,5,1,2']
 ['2012-01-01' '274574' '2,5,4,7,6,10,8,1,9,3']
 ['2012-01-01' '274573' '8,4,6,3,2,9,5,10,1,7']]
'''

# 2、创建矩阵
a1 = np.array([1,2,3])             # 创建一维矩阵
a2 = np.array([[1,2,3],[1,2,3]])   # 创建一个二维矩阵
print(a1.shape)                   # 查看矩阵的结构 (3,)  3行1列
print(a2.shape)                   # 查看矩阵的结构 (2,3) 2行3列

# 3、类型转换
## numpy array传入的值必须同一类型，不然会自动转换成为较少数量的数值类型
b1 = np.array([1,2,3,4])
b2 = np.array([1,2,3,4.])
b3 = np.array([1,2,3,'4'])
print(b1.dtype)                   # int32
print(b2.dtype)                   # float64
print(b3.dtype)                   # <U11

# 4、选取数据
## 和python使用方法一样
c1 = np.genfromtxt("../pk10.txt",delimiter="	",dtype="str")
print(c1[1,2])                    # 5,9,10,4,2,7,3,6,8,1
print(c1[2,1])                    # 656196

# 5、切片
d1 = np.array([5,10,15,20])
print(d1[0:3])                    #  [5,10,15] 切片切取0到3的数据 不包括3
d2 = np.array([
    [5,10,15],
    [20,25,30],
    [30,35,40]
])
print(d2[:,1])                    # [10 25 35] 切片切取整个数据结构的下标为1的列

# 6、对Numpy结构一次操作会同步给每一个
e1 = np.array([5,10,15,20])
## 如进行一个判断操作，就可以对每个对象进行相同操作，就不用for循环
print(e1 == 10)                      # array([False,  True, False, False], dtype=bool)
e2 = np.array([
    [5,10,15],
    [20,25,30],
    [30,35,40]
])
print(e2 == 10)
'''
array([[False,  True, False],
       [False, False, False],
       [False, False, False]], dtype=bool)
'''
## 将判断的布尔值作为参数传入数据对象
e3 = (e1 == 10)
print(e1[e3])                     # [10]
e4 = (e2[:,1] == 25)
print(e2[e4,:])                   # [[20,25,30]]

# 7、或 与 操作
f1 = np.array([5,10,15,20])
f2 = (f1 == 10) & (f1 == 5)        # 与 操作 array([False, False, False, False], dtype=bool)
f3 = (f1 == 10) | (f1 == 5)        # 或 操作 array([ True,  True, False, False], dtype=bool)

# 8、改变numpy.array的数据类型
g1 = np.array(['1','2','3'])
g2 = g1.astype(float)
print(g1.dtype)                    #  <U1
print(g2.dtype)                    #  float64
print(g2)                          #  array([ 1.,  2.,  3.])

# 9、最小值最大值
h1 = np.array([5,10,15,20])
print(h1.max())                     # 5
print(h1.min())                     # 20
## 了解更多属性  print(help(np.array))

# 10、指定维度计算
i1 = np.array([
    [5,10,15],
    [20,25,30],
    [30,35,40]
])
i2 = i1.sum(axis = 1)                    # array([ 30,  75, 105]) 若axis=1 则按行计算每一行的和
i3 = i1.sum(axis = 0)                    # array([55, 70, 85])    若axis=0 则按列计算每一列的和

# 11、数据结构变换
j1 = np.arange(15)                       # np.aramge 创建出来的是向量格式
j2 = j1.reshape(3,5)                     # reshape 是将向量转换成指定格式的矩阵
'''
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
'''
j2.shape                                 # 矩阵结构 (3,5)
j2.ndim                                  # 矩阵维度  2
j2.dtype.name                            # 矩阵数据类型 'int32'
j2.size                                  # 矩阵长度  15

# 12、初始化一个矩阵，值都是0
k1 = np.zeros((3,4))                     # 初始化矩阵结构为 (3,4)
'''
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])
'''

# 13、初始化一个矩阵，值都是1
k2 = np.ones((2,3,4),dtype=np.int32)     # 初始化矩阵结构为 (2,3,4) 且数据是int32
'''
array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]])
'''

# 14、arange数据间隔
k3 = np.arange( 10,30,5 )                 #  array([10, 15, 20, 25])
# 介绍 np.arange(start,end,skip) 开始，结束，跳过  且不包含end值
k4 = np.arange(12).reshape(4,3)
'''
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]])
'''

# 15、随机数的使用
l1 = np.random.random((2,3))              # 随机数返回的是矩阵，这里设置矩阵结构
'''
array([[ 0.25731809,  0.14592857,  0.1125052 ],
       [ 0.94415331,  0.46446762,  0.26658256]])
'''
from numpy import pi
l2 = np.linspace( 0, 2*pi, 100)           # np.linspace(start,end,total)
## linspace生成的是从start到end中平均取total个数据
