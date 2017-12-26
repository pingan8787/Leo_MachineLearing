'''
tensorflow程序通常被组织成一个图的构建和图的执行阶段。
例如我们搭建一个神经网络，组织各个层及之间关系的过程称为图的构建，然后通过不断反复的执行图中的训练op来逐渐优化参数。
在图的构建阶段，就是各种op的拼接组合，op之间流通的tensor是由最初的一个op产生的，它被称为源op，没有输入tensor，只有输出tensor，比如说常量(Constant)就是一个源op：
'''


import tensorflow as tf

matrix1 = tf.constant([[3.,4.]])
matrix2 = tf.constant([[5.],[6.]])
product = tf.matmul(matrix1,matrix2)
with tf.Session() as sess:
    print(sess.run(product))

'''
我们这样就创建了一个最简单的图，图的输出端口为product，这个图包含了三个op，两个源constant()op,一个matmul()op，如果要想真正的执行得到乘法之后的结果，需要运行会话，然后获取product的值。Session对象在使用完之后需要手动关闭close()，也可以使用‘with’让程序自动的执行完之后关闭。
'''



# g1 = tf.Graph()
# with g1.as_default():
#     v = tf.get_variable("v",initializer=tf.zeros_initializer(shape=[1]))

