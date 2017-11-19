
#coding:utf-8
# 1/高阶函数 map()
## 为list每个值执行相同函数操作,只有一个参数
def f(x):
    return x*x
print map(f,[1,2,3,4,5,6]) # 得到一个新list

def format_name(name):
    return name[:1].upper() + name[1:].lower()
print map(format_name,['leo','lEo','leO'])

# 2/高阶函数 reduce()
## 为list每个值执行相同函数操作,最少两个参数
def g(x,y):
    return x+y
print reduce(g,[1,2,3,4,5,6])

def prod(x,y):      # 求积函数
    return x*y
print reduce(prod,[1,2,3,4,5,6],100)   # 第三个参数为初始值

# 3/高阶函数 filter()
## 为list每个值执行过滤操作,只要一个参数
def is_odd(x):      # 过滤list中的偶数，保留奇数
    return x%2==1
print filter(is_odd,[1,2,3,4,5,6])

def is_empty(x):    # 过滤list中的空值，保留存在值
    return x and len(x.strip())>0
print filter(is_empty,['leo',None,'123',' ','','END'])

import math
def is_sqr(x):     # 过滤1-100中平方根是整数的数
    sqr = int(math.sqrt(x))
    return sqr*sqr == x
print filter(is_sqr,range(1,101))

# 4/高阶函数 sorted()
## 自定义排序，x在前y在后 返回-1，反之返回1，相同返回0
test_sort = [36, 5, 12, 9, 21]
string_sort = ['bob', 'about', 'Zoo', 'Credit']
print sorted(test_sort)
print sorted(string_sort)

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