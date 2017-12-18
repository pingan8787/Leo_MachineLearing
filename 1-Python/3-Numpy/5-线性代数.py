# 一、线性代数
## 计算矩阵乘法 dot函数
import numpy as np

a1 = np.array([[1.,2.,3.],[4.,5.,6.]])
a2 = np.array([[6.,23.],[-1,7],[8,9]])
a3 = a1.dot(a2)              # array([[28., 64.],[67.,181.]]) 相当于np.dot(a1,a2)
### 一个二位数组和一个一维数组的矩阵点积运算得到一个一维数组
a4 = np.dot(a1,np.ones(3))   # array([  6.,  15.])

## numpy.linalg 计算一组标准的矩阵分解运算，以及求逆和行列式等

from numpy.linalg import inv,qr
b1 = np.random.randn(5,5)    # 这三个结果值太长，就不写出来
b2 = b1.T.dot(b1)
b3 = inv(b2)
b4 = b2.dot(inv(b2))