###  demo  计算预测 y = 0.1x + 0.3 曲线位置  ###
import tensorflow as tf
import numpy as np

# creat data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

### creat tensorflow structure start ###
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))  
# 定义参数变量(对应上面0.1的位置)，随机数列生成的方式，1纬结构，初始值取值-1.0到1.0
biases = tf.Variable(tf.zeros([1]))
# (对应上面0.3的位置)

y = Weights * x_data + biases
# 预测的y
loss = tf.reduce_mean(tf.square(y-y_data))
# 误差：预测值和真实值的差别  
optimizer = tf.train.GradientDescentOptimizer(0.5)
# 优化器：减小每次计算误差，提升参数准确性
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
# 将变量初始化到神经网络
### creat tensorflow structure end   ###

sess = tf.Session()
sess.run(init)
# 激活神经网络 非常重要

for step in range(201):
    sess.run(train)
    if step %20 == 0:
        print(step,sess.run(Weights),sess.run(biases))


'''
0 [ 0.14649083] [ 0.35748428]
20 [ 0.10346913] [ 0.29830638]
40 [ 0.10080876] [ 0.29960519]
60 [ 0.10018856] [ 0.29990795]
80 [ 0.10004395] [ 0.29997855]
100 [ 0.10001026] [ 0.29999501]
120 [ 0.10000238] [ 0.29999885]
140 [ 0.10000055] [ 0.29999974]
160 [ 0.10000012] [ 0.29999995]
180 [ 0.10000011] [ 0.29999995]
200 [ 0.10000011] [ 0.29999995]
'''