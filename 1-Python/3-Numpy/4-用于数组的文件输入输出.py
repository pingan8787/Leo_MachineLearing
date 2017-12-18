# 一、将数组以二进制格式保存到磁盘
## 读写磁盘数组的两个函数 np.save 和 np.load
## 默认情况，数组是以未压缩的原始二进制格式保存在拓展名为.npy文件中。
import numpy as np
a1 = np.arange(10)
np.save('test1',a1)           # 生成文件  即可在当前运行目录中生成 test1.npy 文件
np.load('test1.npy')          # 读取文件