# 文档中的 Python 示例使用一个会话 Session 来 启动图, 并调用 Session.run() 方法执行操作.
# 为了便于使用诸如 IPython 之类的 Python 交互环境, 可以使用 InteractiveSession 代替 Session 类
# 使用Tensor.eval() 和 Operation.run() 方法代替 Session.run() . 这样可以避免使用一个变量来持有会话.

import tensorflow as tf
sess = tf.InteractiveSession()

x = tf.Variable([1.0,2.0])
a = tf.constant([3.0,3.0])

# 使用初始化器 initializer op 的 run() 方法初始化 'x'
x.initializer.run()

# 增加一个减法 sub op 从'x'减去'a'，运行减法op，输出
sub = tf.subtract(x,a)  # sub方法已被替代成 subtract
print(sub.eval())       # [-2. -1.]