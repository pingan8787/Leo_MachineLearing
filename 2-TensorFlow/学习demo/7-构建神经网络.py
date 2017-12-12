### demo 添加层操作 ###
import tensorflow as tf
import numpy as np

# 定义一个函数功能(添加神经层)
def add_layer(inputs,in_size,out_size,activation_function=None):
    # 定义一个权重  in_size行out_size列的矩阵
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    # 定义一个列表  1行out_size列的矩阵
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    # 定义一个乘法 矩阵的乘法
    Wx_plus_b = tf.matmul(inputs,Weights)+biases
    # 开始激活  None则为线性方程 反之非线性方程
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# x_data是(-1,1)区间 一个300行 有300个例子
x_data = np.linspace(-1,1,300)[:,np.newaxis]
# 添加noise 噪点  方差0.05
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32,[None,1])  # tf.float32 记得定义格式
ys = tf.placeholder(tf.float32,[None,1])

## 大概神经元示例如下： 
##   输入层     神经元      输出层
##     1个       10个        1个

# 定义隐藏层 输出l1   
##  add_layer(输入值，输入值长度，输出值长度（神经元数量）,激励函数)
l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)

# 定义输出层 接收l1
prediction = add_layer(l1,10,1,activation_function=None)

# 计算误差
## reduce_mean 求平均 reduce_sum 求和  square 求平方
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))

# 定义训练集
## GradientDescentOptimizer(学习效率)  minimize() 提升误差
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 初始化所有
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i % 50:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))