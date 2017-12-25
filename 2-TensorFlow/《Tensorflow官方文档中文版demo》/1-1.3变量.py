# 实现简单计数器

# 1.创建一个变量，初始化为标量 0
import tensorflow as tf
state = tf.Variable(0,name="counter")

# 2.创建一个 op ，使 state 增加 1
one = tf.constant(1)
new_value =tf.add(state,one)
update = tf.assign(state,new_value)

# 3.所有变量都要初始化 (init) op
init_op = tf.initialize_all_variables()

# 4.启动图，运行 op 
with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(state))
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
