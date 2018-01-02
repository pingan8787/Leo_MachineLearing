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

# 改变numpy.array的数据类型
g1 = np.array(['1','2','3'])
g2 = g1.astype(float)
print(g1.dtype)                    #  <U1
print(g2.dtype)                    #  float64
