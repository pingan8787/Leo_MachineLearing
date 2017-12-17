# 一、利用数组进行数据处理 
## 用数组表达式代替循环的方法称为矢量化。
p1 = np.arange(-5,5,0.01)   # 1000个间隔相同的点
xs,ys = np.meshgrid(p1,p1)  # 从坐标向量返回坐标矩阵。
ys
import matplotlib.pypolt as plt
p2 = np.sqrt(xs **2 + ys ** 2)
p2
### array([[ 7.07106781,  ..., 7.05693985,  7.06400028],
###        ...,
###        [ 7.06400028,  ..., 7.04985815,  7.05692568]])
plt.imshow(p2,cmap=plt.cm.gray);
plt.colorbar()
plt.title('第一个图，image plot of $\sqrt{x^2 + y^2}$ for a grid of values')
plt.show()                   # 显示图片

# 二、将条件逻辑表述为数组运算
## numpy.where函数是三元表达式 x if condition else y 的矢量化版本。
## numpy.where(condition[, x, y]) condition是条件 x,y(可选)需要选择的值
ax = np.array([1.1,1.2,1.3,1.4,1.5])
ay = np.array([2.1,2.2,2.3,2.4,2.5])
ac = np.array([True,False,True,True,False])
## 实现 当ac中的值为True则取ax的值，反之去ay的值
ar = np.where(ac,ax,ay)     # 根据条件，从x或y返回元素。
ar                          # array([ 1.1,  2.2,  1.3,  1.4,  2.5])

ax1 = np.random.randn(4,4)        
### array([[ 0.96148606,  2.15145482,  0.59473811, -0.63179309],
###        [ 0.11569812, -0.43374087, -0.55493693, -1.82742267],
###        [ 0.37992965,  1.30423439,  1.04124003, -0.0080651 ],
###        [ 0.04254254,  0.70302227,  1.24916566, -0.49637547]])
ac1 = np.where(ax1 > 0,2,ax1)
### array([[ 2.        ,  2.        ,  2.        , -0.63179309],
###        [ 2.        , -0.43374087, -0.55493693, -1.82742267],
###        [ 2.        ,  2.        ,  2.        , -0.0080651 ],
###        [ 2.        ,  2.        ,  2.        , -0.49637547]])

# 三、数学和统计方法
## 通过数组上的一组数字函数对整个数组或某个轴向的数据进行统计计算。
b1 = np.random.rand(5,4)     # 正态分布的数据
## mean(a,axis,..) 沿指定轴计算算术平均值 a指定数据 axis指定轴向
b2 = b1.mean()               # 0.49534416621330496
b3 = np.mean(b2)             # 0.49534416621330496 写法跟 b2 = b1.mean() 一致
b4 = b1.sum()                # 9.906883324266099
## mean()和sum()这类函数可接收一个axis参数，最终结果是一个少一维的数组
b5 = b1.mean(axis = 1)       # array([ 0.52252766,  0.43953336,  0.46266831,  0.52721901,  0.66995639])
b6 = b1.sum(0)               # array([ 3.05852217,  3.25553911,  2.14468495,  2.02887274])
## 另外还有：
## 默认情况下，平均数取平展数组，否则在指定轴上。
b7 = np.array([[1,2],[3,4]]) 
b8 = b7.mean()               # 2.5  算术平均值是沿着轴的元素的总和除以元素的数量。
b9 = b7.mean(axis=1)         # array([ 1.5,  3.5]) 计算第一行
## 总结数学和统计方法，常见的有 sum/mean/std/var/min/max/argmin/argmax/cumsum/sumprod
## 详细内容查看手册

# 四、用布尔型数组的方法
## 上述方法中布尔值会被强制转换成1(True)和0(False)
### 1、sum常被用来对布尔型数组中True的计数
c1 = np.random.randn(100)
c2 = (c1 > 0).sum()           # 55 正值的数量
### 2、any用于测试数组中是否存在一个或多个True
d1 = np.array([False,False,True,False])
d2 = d1.any()                 # True
### 3、all用于检查数组中所有值是否为True
d3 = d1.all()                 # False
