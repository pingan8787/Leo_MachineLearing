import tensorflow as tf

# 创建一个常量，产生一个 1*2 矩阵，这个op被作为一个节点
a1 = tf.constant([[3.,3.]])
# 创建另一个常量，长生一个 2*1 矩阵
a2 = tf.constant([[2.],[2.]])

# 创建一个矩阵乘法的 matmul op 把a1 a2作为输入
a3 = tf.matmul(a1,a2)

sess = tf.Session()

# 调用run方法执行矩阵乘法的op
a4 = sess.run(a3)
print(a4)

# 执行完毕，关闭会话
sess.close()

####
# 也可以使用 with 代码块来自动关闭 Session
####
with tf.Session() as sess:
    a4 = sess.run([a3])
    print(a4)
    
# **另外可以使用 with..Device 语句指派特定的 CPU 或 GPU 执行操作：
with tf.Session() as sess:
    with tf.device("/cpu:0"):
        b1 = tf.constant([[3.,3.]])
        b2 = tf.constant([[2.],[2.]])
        b3 = tf.matmul(b1,b2)
        b4 = sess.run([b3])
        print(a4)
## 目前支持设备： "/cpu:0":机器的CPU ；"/gpu:0":机器第一个GPU，如果有的话 ; "/gpu:1":机器的第二个GPU 以此类推
        