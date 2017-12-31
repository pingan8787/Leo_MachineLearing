import tensorflow as tf

# 声明2个变量，并通过seed设置随机种子
w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

# xx 输入值的特征向量，暂时定为常量，为1*2矩阵
x = tf.constant([[0.7,0.9]])

# 通过前面描述的前向传播算法，获得神经网络的输出
a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

sess = tf.Session()
# 因为w1 w2还没运行初始化过程，所以不能直接sess.run(y)获取y值。
sess.run(w1.initializer)
sess.run(w2.initializer)

# 获取y值
print(sess.run(y))  # [[ 3.95757794]]
sess.close()

#############################################

## 升级版  通过placeholder写法：
import tensorflow as tf

# 声明2个变量，并通过seed设置随机种子
w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

# xx 输入值的特征向量，暂时定为常量，为1*2矩阵
# 若这里使用的是 n*m 矩阵，则在feed_dict也要传入对应格式数据
x = tf.placeholder(tf.float32, shape=(1,2), name="input")

# 通过前面描述的前向传播算法，获得神经网络的输出
a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

sess = tf.Session()
init_op = tf.global_variables_initializer()
# initialize_all_variables被 global_variables_initializer 代替
sess.run(init_op)

# 获取y值
print(sess.run(y,feed_dict={x:[[0.7,0.9]]}))  # [[ 3.95757794]]
sess.close()
