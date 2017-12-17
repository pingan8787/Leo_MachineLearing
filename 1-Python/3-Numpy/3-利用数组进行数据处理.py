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