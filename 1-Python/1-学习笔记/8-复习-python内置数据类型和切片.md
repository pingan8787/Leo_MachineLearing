# python内置数据类型
## 1、list
一种有序集合，可以随意添加删除元素。  
```
建：leo = ['name','age','count']
查：leo[0]     # 'name'
    leo[-1]    # 'count'
增：leo.append('height')
    leo.insert(0,'width')    # 参数： 插入索引位置，待添加元素
删：leo.pop()                 # 删除最后一个，并放回该元素
   leo.pop(index)            # 删除指定索引，并返回该元素
改：leo[0] = 'test'
```

## 2、tuple 
称为"元组"，一但创建不可修改。  
```
建：t1 = ()    # 创建空tuple
   t1 = (1)    # 错误写法  应该写成 t1 = (1,)
改： # 不能修改，但可以这样修改
    t2 =('a','b',['A','B'])
    t3 = t2(2)
    t3[0]='X'
```

## 3、dict 
标识"键-值",key不可重复,通过key查到value。  
```
建：d1 = {"name":leo,"age":25}    len(d1) # 获取集合大小
查：d1['name']
      # 判断key是否存在，使用in操作符或 get方法
改/增：d1['name']= 'good'  # 若没有这个key则会创建新key
```

## 4、set 
类似list但是元素不能重复(若有则自动去掉)，而且无序。  
```
建：s1 = set(['a','b','c'])   # 常用在去重   len(s1)
增：s1.add('d')
删：s1.remove('d')
遍历：
s1 = set(['a','b','c','d'])  
for n in s1:
  print(n)

s2 = ([('a',12),('b',13),('c',14)])
for n in s2:
  print(s1[0],":",s1[1])
```


# python切片
## 1、list 切片
```
a[0:3]      索引0开始 到 索引3结束，不包括索引3
a[:3]       索引从0开始，可以省略，不包括索引3
a[3:]       索引从3开始，到结束，包括索引3
a[:]        索引从头到尾
a[::2]      索引从头到尾，间隔2个取一次
a[-2:]      索引从倒数第2个到结束
a[:-2]      索引从头到倒数第2个结束
a[-4:-1:2]  索引从倒数第4个到倒数第1个，间隔2个取
```

## 2、tuple 切片
和 list 切片相同。  

## 3、字符串 切片
```
'ABCDEFGH'[:3]   # ABC
'ABCDEFGH'[-3:]  # FGH
'ABCDEFGH'[::2]  # ACEG
```