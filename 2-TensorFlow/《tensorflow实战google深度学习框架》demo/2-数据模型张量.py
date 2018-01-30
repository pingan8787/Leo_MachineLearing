## tensorflow 所有数据都是通过张量的形式来表示。
## 功能上，张量可以简单理解为多维数组。其中，零阶张量表示标量，也就是一个数。
## 第一阶张量为向量，即一个一维数组
## 第n阶张量理解为n维数组。
## 张量中没有真正保存数字，而是对tensorflow运算结果的引用。

import tensorflow as tf
# tf.constant是一个计算 这个计算的结果是一个张量 保存在变量a中。
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([1.0, 2.0], name="b")
result = tf.add(a, b, name="add")
print(result)
## Tensor("add:0", shape=(2,), dtype=float32)
## （张量的标识符  张量的维度   张量的类型）


## 张量的使用
## 第一类用途  对中间计算结果的引用，如：
### 有使用张量
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([1.0, 2.0], name="b")
result = a + b
### 没有使用张量
result = tf.constant([1.0, 2.0], name="a") + tf.constant([1.0, 2.0], name="b")