# 一、线性代数
## numpy线性代数API手册  python.usyiyi.cn/translate/NumPy_v111/reference/routines.linalg.html
## 计算矩阵乘法 dot函数
import numpy as np

a1 = np.array([[1.,2.,3.],[4.,5.,6.]])
a2 = np.array([[6.,23.],[-1,7],[8,9]])
a3 = a1.dot(a2)              # array([[28., 64.],[67.,181.]]) 相当于np.dot(a1,a2)
### 一个二维数组和一个一维数组的矩阵点积运算得到一个一维数组
a4 = np.dot(a1,np.ones(3))   # array([  6.,  15.])

## numpy.linalg 计算一组标准的矩阵分解运算，以及求逆和行列式等

from numpy.linalg import inv,qr
b1 = np.random.randn(5,5)    # 这三个结果值太长，就不写出来
b2 = b1.T.dot(b1)
b3 = inv(b2)                 # linalg.inv 计算矩阵的（乘法）逆。
b4 = b2.dot(inv(b2))
q,r = qr(b2)                 # linalg.qr 计算矩阵的qr因式分解。

### 更多常用的numpy.linalg函数查看手册
### diag/dot/trace/det/eig/inv/pinv/qr/svd/solve/lstsq/

### 外积/内积介绍：http://blog.csdn.net/dcrmg/article/details/52416832
### 1.向量点乘(内积)： 
### 向量的点乘,也叫向量的内积、数量积、点积，对两个向量执行点乘运算，就是对这两个向量对应位一一相乘之后求和的操作，点乘的结果是一个标量。
### 要求一维向量a和向量b的行列数相同。
### 公式：设：a = [a1,a2,..,an] b = [b1,b2,..,bn]  a和b的点积公式：a·b = a1b1+a2b2 + ... + anbn
### 2.叉乘(外积/向量积) 
### 两个向量的叉乘，又叫向量积、外积、叉积，叉乘的运算结果是一个向量而不是一个标量。并且两个向量的叉积与这两个向量组成的坐标平面垂直。
