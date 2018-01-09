import pandas as pd
import numpy as np

titanic = pd.read_csv('../train.csv')
titanic.head()

"""
训练数据集有891行12列。各列代表的信息：
· PassengerId：一个用以标记每个乘客的数字id
· Survived：标记乘客是否幸存——幸存(1)、死亡(0)。我们将预测这一列。
· Pclass：标记乘客所属船层——第一层(1),第二层(2),第三层(3)。
· Name：乘客名字。
· Sex：乘客性别——男male、女female
· Age：乘客年龄。部分。
· SibSp：船上兄弟姐妹和配偶的数量。
· Parch：船上父母和孩子的数量。
· Ticket：乘客的船票号码。
· Fare：乘客为船票付了多少钱。
· Cabin：乘客住在哪个船舱。
· Embarked：乘客从哪个地方登上泰坦尼克号。
"""

age = titanic['Age']
print(age[0:10])

age_is_null = pd.isnull(age)      # isnull()  判断当前值是否是缺失值
age_null_true = age[age_is_null]  # 过滤只有True的数据
age_null_count = len(age_null_true) # 缺失值的数量

## 处理缺失值  计算年龄平均值
mean_age = sum(titanic['Age'])/len(titanic['Age'])  # NAN 若没有过滤nan值就会出现这样的错误

##  计算方法1
good_ages = titanic['Age'][age_is_null == False]    # 过滤nan值
mean_age = sum(good_ages)/len(good_ages)             # 正确计算平均值

## 计算方法2
mean_age = titanic['Age'].mean()

## 计算每个等级票价均值
### 方法1
passenger_classes = [1,2,3]
fares_by_class = {}
for this_class in passenger_classes:
    print(this_class)
    pclass_rows = titanic[titanic['Pclass'] == this_class]
    pclass_fares = pclass_rows['Fare']
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fares_by_class
print(fares_by_class)

### 方法2   数据透视表 pivot_table：用来统计一个量和另外一些量的关系
#### 获取每个等级仓位票价的平均值
passenger_survival = titanic.pivot_table(index="Pclass",values="Survived",aggfunc=np.mean)
print(passenger_survival)
#### 获取每个等级仓位用户的年龄平均值
passenger_age = titanic.pivot_table(index="Pclass",values="Age")  # aggfunc默认按照np.mean计算平均值
#### 判断一个量和两个量的关系 当前登船地方和票价还有是否被救的关系
port_stats = titanic.pivot_table(index="Embarked",values=["Fare","Survived"],aggfunc=np.sum)