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
ax = np.array([1.1,1.2,1.3,1.4,1.5])
ay = np.array([2.1,2.2,2.3,2.4,2.5])
ac = np.array([True,False,True,True,False])
## 实现 当ac中的值为True则取ax的值，反之去ay的值
ar = np.where(ac,ax,ay)
ar             # array([ 1.1,  2.2,  1.3,  1.4,  2.5])