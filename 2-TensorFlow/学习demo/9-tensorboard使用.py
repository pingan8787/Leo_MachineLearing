## demo 可视化好助手tensorboard ##
import tensorflow as tf

# 定义一个函数功能(添加神经层)
def add_layer(inputs,in_size,out_size,activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            # 定义一个权重  in_size行out_size列的矩阵
            Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')  # ** name是显示在图形上的标题
        
        with tf.name_scope('biases'):
            # 定义一个列表  1行out_size列的矩阵
            biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)

        with tf.name_scope('Wx_plus_b'):
            # 定义一个乘法 矩阵的乘法
            Wx_plus_b = tf.add(tf.matmul(inputs,Weights),biases)
        # 开始激活  None则为线性方程 反之非线性方程
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

with tf.name_scope('inputs'): # ** 大框架包含xs,ys
    xs = tf.placeholder(tf.float32,[None,1],name='x_input')  # ** name是显示在图形上的标题
    ys = tf.placeholder(tf.float32,[None,1],name='y_input')

## 大概神经元示例如下： 
##   输入层     神经元      输出层
##     1个       10个        1个

# 定义隐藏层 输出l1   
##  add_layer(输入值，输入值长度，输出值长度（神经元数量）,激励函数)
l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)

# 定义输出层 接收l1
prediction = add_layer(l1,10,1,activation_function=None)

# 计算误差
with tf.name_scope('loss'):
    ## reduce_mean 求平均 reduce_sum 求和  square 求平方
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))

# 定义训练集
with tf.name_scope('train'):
## GradientDescentOptimizer(学习效率)  minimize() 提升误差
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 初始化所有
sess = tf.Session()

# 将整个框架加载到一个文件 在展示出来  graph表示全部内容
## 在1.0版本中，tf.train.SummaryWriter已经改为tf.summary.FileWriter
writer = tf.summary.FileWriter('logs/',sess.graph)
sess.run(tf.initialize_all_variables())