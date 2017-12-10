###  demo session会话的2种打开方式  ###
import tensorflow as tf

matrix1 = tf.constant([[3,3]])
# 创建一个一行两列常量的矩阵
matrix2 = tf.constant([[2],[2]])
# 创建一个一列两行常量的矩阵
product = tf.matmul(matrix1,matrix2)
# 计算矩阵乘法 形式 np.dot(m1,m2)

# #方式1
# sess = tf.Session()
# result = sess.run(product)
# print(result)      ## [[12]]
# sess.close()

# 方式2   会自动关闭sess
with tf.Session() as sess :
    result2 = sess.run(product)
    print(result2)    ## [[12]]
# 写后面的操作
