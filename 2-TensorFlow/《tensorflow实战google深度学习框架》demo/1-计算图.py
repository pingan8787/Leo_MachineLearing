## 1、计算图的使用
'''
tensorflow 程序一般有两个计算，第一个阶段需要定义计算图中所有的计算。第二个阶段是执行计算。
'''
import tensorflow as tf
## 定义第一阶段
a = tf.constant([1.0, 2.0], name="计算图a")
b = tf.constant([3.0, 4.0], name="计算图b")
result = a + b
## 定义第二阶段
sess = tf.Session()
sess.run(result)  #  array([ 4.,  6.], dtype=float32)

## 2、获取默认计算图
'''
tensorflow会自动将定义的计算转化为计算图上的节点，在tensorflow程序中，系统会自动维护一个默认的计算图，通过tf.get_default_graph函数可以获取当前默认的计算图。
下面代码演示如何获取默认计算图以及如何查看一个运算所属的计算图。
通过a.graph可以查看张量所属的计算图，因为没有特意指定，所以这个计算图应该等于当前默认的计算图，所以下面这个操作输出值为True
'''
print( a.graph is tf.get_default_graph() )  # True

## 3、生成计算图
###  tensorflow 支持通过 tf.Graph 函数生成新的计算图，不同计算图上的张量和运算都不会共享，所以下面代码演示如何在不同计算图上定义和使用变量。
import tensorflow as tf
g1 = tf.Graph()
with g1.as_default():
    # 在计算图g1中定义变量“v” 并设置初始值为0
    v = tf.get_variable("v", shape=[1], initializer=tf.zeros_initializer)

# 在计算图g1中取得变量“v”
with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("",reuse=True):
        # 在计算图g1中，变量v的取值应该为0，所以下面这行输出[0.]
        print(sess.run(tf.get_variable("v")))   # [ 0.]

## 4、指定GPU设备运行
g = tf.Graph()
with g.device("/gpu:0"):
    result = a+ b


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


