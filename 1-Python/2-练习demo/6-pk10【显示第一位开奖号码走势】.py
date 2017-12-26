import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser

## 设置figure的字体和显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

df_pk10 = pd.read_csv('./txt/pk10.csv')
df_pk10 = df_pk10[:100]    # 先拿1000条数据
# print(df_pk10)

# 这是是打算将每个开奖期号数据从str转成arr
# for i in df_pk10:
#     print(df_pk10[i])

# 转化opennums 并 用opennums接收
opennums = df_pk10['opennums']
section = df_pk10['section']
open_result1 = []
# open_result2 = []
# open_result3 = []

# print(opennums)
for i in opennums:
    open_result1.append((i.split(','))[0])
    # open_result2.append((i.split(','))[1])
    # open_result3.append((i.split(','))[2])

print(open_result1)
print(section)

# fig,ax = plt.subplots()

# plt.xticks(rotation=70)

# ax.xaxis.set_major_formatter(section)

# ax.plot(opennums,open_result1,'r')
# fig

## 开始画图  参考文章《python用matplotlib画折线图》   blog.csdn.net/hecongqing/article/details/55522276

plt.figure()
plt.plot(section,open_result1,label="第1位",linewidth=2,color='r',marker='o',markerfacecolor="blue",markersize=6)
# plt.plot(section,open_result2,label="第2位",linewidth=2,color='m',marker='x',markersize=6)
# plt.plot(section,open_result3,label="第3位",linewidth=2,color='c',marker='+',markersize=6)
plt.xlabel('section')
plt.ylabel('ball-1') 
plt.title('This is the first number of the PK10 game history')
plt.legend()
plt.show()