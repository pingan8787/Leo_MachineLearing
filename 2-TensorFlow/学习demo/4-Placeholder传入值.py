### demo 传入值 placeholder  ###
import tensorflow as tf

# tensorflow 定义一个placeholder
input1 = tf.placeholder(tf.float32)  # 定义结构2行2列
# input1 = tf.placeholder(tf.float32,[2,2])  # 定义结构2行2列

input2 = tf.placeholder(tf.float32)

# tensorflow 定义一个乘法运算 tf.mul(...)
output = tf.multiply(input1,input2)  # tf.mul()已被tf.multiply()替代

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))  #  [ 14. ]
# 用了placeholder就必须在feed_dict中绑定传入值