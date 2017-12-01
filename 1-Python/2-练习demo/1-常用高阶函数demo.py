
#coding:utf-8
# 1、高阶函数 map()
## 为list每个值执行相同函数操作,只有一个参数
def f(x):
    return x*x
print map(f,[1,2,3,4,5,6])            # 得到一个新list

print list(map(str,[1,2,3,4,5,6]))    # str是自带函数，将内容设置为string类型

def format_name(name):
    return name[:1].upper() + name[1:].lower()
print map(format_name,['leo','lEo','leO'])

# 2、高阶函数 reduce()
## 为list每个值执行相同函数操作,最少两个参数
## reduce把结果继续和序列的下一个元素做 累积计算，如本次这个和下次一个一起算
from functools import reduce
def g(x,y):                            # 求和函数
    return x+y
print reduce(g,[1,2,3,4,5,6])          
## 求和运算可以直接用Python内建函数sum()，没必要动用reduce。

from functools import reduce
def prod(x,y):                         # 求积函数
    return x*y
print reduce(prod,[1,2,3,4,5,6],100)   # 第三个参数为初始值

## 案例
## 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
from functools import reduce
def normalize(name):
    return name[:1].upper()+name[1:].lower();
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 3、高阶函数 filter()
## 为list每个值执行过滤操作,只要一个参数，filter()函数用于过滤序列。
def is_odd(x):          # 过滤list中的偶数，保留奇数
    return x%2==1
print filter(is_odd,[1,2,3,4,5,6])

def is_empty(x):        # 过滤list中的空值，保留存在值
    return x and len(x.strip())>0
print filter(is_empty,['leo',None,'123',' ','','END'])

import math
def is_sqr(x):          # 过滤1-100中平方根是整数的数
    sqr = int(math.sqrt(x))
    return sqr*sqr == x
print filter(is_sqr,range(1,101))

def primes():           # 一个计算100以内素数的函数
    yield 2
    it = _odd_iter()    # 初始序列
    while True:
        n = next(it)    # 返回序列的第一个数
        yield n
        it = filter(_odd_iter(n),it)  # 构造新序列
for n in primes():      # 由于primes()是一个无限序列，所以调用时需设置一个退出循环的条件：
    if n <1000:
        print(n)
    else:
        break 

# 4、高阶函数 sorted()
## 自定义排序，x在前y在后 返回-1，反之返回1，相同返回0
test_sort = [36, 5, 12, 9, 21]
string_sort = ['bob', 'about', 'Zoo', 'Credit']
abs_sort = [36, 5, -12, 9, -21]
print sorted(test_sort)
print sorted(string_sort)
## sorted()函数是一个高阶函数，还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print sorted(abs_sort,key = abs)
print sorted(string_sort,key = str.lower)
## 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print sorted(string_sort,key = str.lower, reverse=True)

def is_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
sorted(test_sort,is_cmp)

def sort_string(s1,s2):     # 实现不区分大小写的字符串排序
    str1 = s1.upper()
    str2 = s2.upper()
    if str1 < str2:
        return -1
    if str1 > str2:
        return 1
    return 0
print sorted(string_sort,sort_string)