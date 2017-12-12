### demo 添加层操作 ###
import tensorflow as tf

### 定义一个函数功能(添加神经层) ###
def add_layer(inputs,in_size,out_size,activation_function=None):
    # 定义一个权重  in_size行out_size列的矩阵
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    # 定义一个列表  1行out_size列的矩阵
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    # 定义一个乘法 矩阵的乘法
    Wx_plus_b = tf.matmul(inputs,Weights)+biases
    # 开始激活  None则为线性方程 反之非线性方程
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs
