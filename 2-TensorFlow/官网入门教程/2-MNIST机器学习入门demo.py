# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 09:03:11 2017

@author: Administrator
"""

import input_data
mnist = input_data.read_data_sets('MNIST',one_hot=True)

import tensorflow as tf

# 1/ placeholder表示一个占位符，将来运行可以传入新值
x = tf.placeholder("float",[None,784])     

# 2/ Variable表示一个可修改的张量，可以计算输入值也可以修改，一般用与模型参数
# 3/ zeros[m,n] 可以生成 m,n 型矩阵，如 [2,3],int32) => [[0,0,0],[0,0,0],[0,0,0]]
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

# 4/ nn为 NeuralNetwork 神经网络 ， matmul 矩阵相乘
y = tf.nn.softmax(tf.matmul(x,W)+b)
y_ = tf.placeholder("float",[None,10])

# 5/ reduce_sum() 计算一个张量的各个维度的元素的和。
cross_entropy = -tf.reduce_sum(y_*tf.log(y))

# 6/ GradientDescentOptimizer(0.01)梯度下降算法，0.01的学习速率最小化交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# 训练模型
for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={x:batch_xs ,y_:batch_ys})
    
# 评估模型
# 7/ tf.argmax(y,1)返回的是模型对于任一输入x预测到的标签值
# 8/ tf.argmax(y_,1) 代表正确的标签
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

# 9/ tf.reduce_mean()计算一个张量的各个维度的元素的平均值。
# 10/ tf.cast()将一个张量投射到一个新的类型。
accuracy = tf.reduce_mean(tf.cast(correct_prediction,"float"))

print(sess.run(accuracy, feed_dict={x:mnist.test.images,y_:mnist.test.labels}))