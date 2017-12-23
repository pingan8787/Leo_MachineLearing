> 文章素材来源网络文章 http://blog.csdn.net/u012162613/article/details/42784403

## 一、初学与入门
### 1、初学者10题
1-在python环境中导入numpy包，并命名为np
```
import numpy as np
```

2-查看numpy版本和配置信息
```
np.__version__
```

3-创建零向量，zeros函数
```
a1 = np.zeros((2,3)) 
## array([[ 0.,  0.,  0.],
##        [ 0.,  0.,  0.]])
```

4-将上面的零向量的第二行第三列元素置为1。注意python中行列都是从0开始。
```
a1[1,2] = 1
## array([[ 0.,  0.,  0.],
##        [ 0.,  0.,  1.]])
```

5-arange函数，创建一个在给定范围的向量
```
a2 = np.arange(1,101)  # 1-100范围不包含101
```

6-reshape函数，将array变形为矩阵
```
a3 = np.arange(9).reshape(3,3)  
## array([[0, 1, 2],
##        [3, 4, 5],
##        [6, 7, 8]])
```

7-nonzero函数，寻找非0元素的下标
```
a4 = np.nonzero([1,2,3,0,0,4,0])  # (array([0, 1, 2, 5], dtype=int64),)
```

8-eye函数，生成单位向量
```
a5 = np.eye(3)
## array([[ 1.,  0.,  0.],
##        [ 0.,  1.,  0.],
##        [ 0.,  0.,  1.]])
```

9-diag函数，diagonal对角线
```
a6 = np.diag([1,2,3,4],k=0)       # k=0，以[1,2,3,4]为对角线
## array([[1, 0, 0, 0],
##        [0, 2, 0, 0],
##        [0, 0, 3, 0],
##        [0, 0, 0, 4]])
a7 = np.diag([1,2,3,4],k=1)       # k=1，以[1,2,3,4]为对角线
## array([[0, 1, 0, 0, 0],
##        [0, 0, 2, 0, 0],
##        [0, 0, 0, 3, 0],
##        [0, 0, 0, 0, 4],
##        [0, 0, 0, 0, 0]])

a8 = np.diag([1,2,3,4],k=-1)       # k=-1，以[1,2,3,4]为对角线
## array([[0, 0, 0, 0, 0],
##        [1, 0, 0, 0, 0],
##        [0, 2, 0, 0, 0],
##        [0, 0, 3, 0, 0],
##        [0, 0, 0, 4, 0]])
```

10-random模块的random函数，生成随机数
```
a9 = np.random.random((3,3))  
## array([[ 0.37607512,  0.62883501,  0.65996391],
##        [ 0.78327199,  0.65893716,  0.70154238],
##        [ 0.0489404 ,  0.53343568,  0.59334416]])
```

### 2、入门级10题
1-创建一个8*8的“棋盘”矩阵
```
r1 = np.zeros((8,8),dtype=int)
r1[1::2,::2] = 1  #1,3,5,7行 2,4,6列的元素设置为1
r1[::2,1::2] = 1  
```

2-min()和max()函数
```
import numpy as np
a2 = np.random.random((10,10))
a2max,a2min = a2.max(),a2.min()
```

3-函数tile(A,reps),reps即重复的次数，不仅可以是数字，还可以是array。比如构造棋盘矩阵：
```
a3 = np.tile(np.array([[0,1],[0,1]]),(4,4))
```

4-归一化，将矩阵规格化到0～1，即最小的变成0，最大的变成1，最小与最大之间的等比缩放。
```
a4 = np.random.random((5,5))
a4max,a4min = a4.max(),a4.min()
a4=(a4-a4min)/(a4max-a4min)
```

5-矩阵点乘
```
a5 = np.dot(np.ones((5,3)),np.ones((3,2)))
## array([[ 3.,  3.],
##        [ 3.,  3.],
##        [ 3.,  3.],
##        [ 3.,  3.],
##        [ 3.,  3.]])
```

6-矩阵相加，5*5矩阵+1*5的向量，相当于每一行都加上1*5矩阵
```
a6 = np.zeros((5,5))
a6 += np.arange(5)
## array([[ 0.,  1.,  2.,  3.,  4.],
##        [ 0.,  1.,  2.,  3.,  4.],
##        [ 0.,  1.,  2.,  3.,  4.],
##        [ 0.,  1.,  2.,  3.,  4.],
##        [ 0.,  1.,  2.,  3.,  4.]])
```

7-linspace函数，在给定区间中生成均匀分布的给定个数。
```
a8 = np.linspace(0,10,11,endpoint=True,retstep=False)
## array([  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.])
## numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
## 生成0~10之间均匀分布的11个数，包括0和1。
## 若endpoint=False,则10不包括在里面。
## 若retstep=False，会同时返回均匀区间中每两个数的间隔。
```

8-sort函数。调用random模块中的random函数生成10个随机数，然后sort排序。
```
a9 = np.random.random(10)  
a9.sort()
## array([ 0.00462968,  0.03209223,  0.07702007,  0.1968538 ,  0.31196594,
##         0.37648172,  0.45438051,  0.56967879,  0.70055142,  0.76796064])
```

9-allclose函数，判断两个array在误差范围内是否相等
```
##  numpy.random.randint(low, high=None, size=None, dtype='l')
##  numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
##  如果两个数组在元素级别在容差内相等，则返回True。
b1 = np.random.randint(0,2,5)
b2 = np.random.randint(0,2,5)
b3 = np.allclose(b1,b2)
## False
```

10-mean函数，求平均值
```
b4 = np.random.random(30)
b5 = b4.mean()
## 0.48059270596771703
```

## 文档手册
[NumPy中文API手册](http://python.usyiyi.cn/translate/NumPy_v111/genindex.html)