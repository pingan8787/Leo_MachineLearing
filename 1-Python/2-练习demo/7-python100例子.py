# 例题来自于 www.runoob.com/python/python-100-examples.html

# 例题1: 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
### 方法1：
a1 = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (j!=k) and (k!=i):
                print(i,j,k)
                a1.append([i,j,k])
print(len(a1))         # 24
### 方法2：
a2_test = [1,2,3,4]
a2 = [i*100 + j*10 + k*1 for i in a2_test for j in a2_test for k in a2_test if ( i!=j) and (j!=k) and (k!=i)]
print(a2)
print(len(a2))
### 方法3： python自带这个函数的
from itertools import permutations
for i in permutations([1, 2, 3, 4], 3):
    print(i)