# 1-python 字符串数组互转

## 字符串转数组
str = '1,2,3'
arr = str.split(',')

## 数组转字符串
arr = ['a','b']
str = ','.join(arr)

arr = [1,2,3]
str = ','.join(str(i) for i in b)