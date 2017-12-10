###  demo 定义变量和初始化所有变量  ###
import tensorflow as tf
# tensorflow定义变量     tf.Variable(...)
state = tf.Variable(0,name='counter')
# print(state.name)   ## counter:0

# tensorflow定义一个常量 tf.constant(...)
one = tf.constant(1)

# tensorflow定义一个加法 tf.add(...)
new_value = tf.add(state , one)

# tensorflow定义一个更新数据  tf.assign(...)
update = tf.assign(state,new_value)  # new_value 更新到 state 上

# tensorflow定义一个初始化所有变量
init = tf.initialize_all_variables()  # 如果有定义变量就一定要使用

with tf.Session() as sess:
    sess.run(init) # 真正意义上的初始化所有变量
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))  # 需要将指针指定到需要打印的变量

'''
1
2
3
'''