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

## 1、计算年龄平均值处理缺失值
mean_age = sum(titanic['Age'])/len(titanic['Age'])  # NAN 若没有过滤nan值就会出现这样的错误

##  计算方法1
good_ages = titanic['Age'][age_is_null == False]    # 过滤nan值
mean_age = sum(good_ages)/len(good_ages)             # 正确计算平均值

## 计算方法2
mean_age = titanic['Age'].mean()

## 2、计算每个等级票价均值
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

## 3、删除所有缺失值 dorpna函数
drop_no = titanic.dropna(axis = 1)
new_titanic = titanic.dropna(axis=0,subset=["Age","Sex"])

## 4、定位具体坐标上面的数据值
row_83_age= titanic.loc[83,"Age"]    # loc[ 行, 列 ]

## 5、重新设置index 用 reset_index( drop=True)
new_titanic_survival = titanic.sort_values("Age",ascending = False)
titanic_reindexed = new_titanic_survival.reset_index( drop=True )
print(titanic_reindexed.loc[0:10])

## 6、自定义函数
### 返回第100个数据
def hundredth_row(column):
    hundredth_item = column.loc[99]
    return hundredth_item
hundredth_row = titanic.apply(hundredth_row)   # 用apply函数来执行 titanic相当于参数column

### 计算所有空值的数量
def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)
column_null_count = titanic.apply(not_null_count)

### 更改船舱等级
def which_class(row):
    pclass = row["Pclass"]
    if pd.isnull(pclass):
        return "Unknow"
    elif pclass == 1:
        return "Frist Class"
    elif pclass == 2:
        return "Second Class"
    elif pclass == 3:
        return "Third Class"
classes = titanic.apply(which_class,axis=1)

### 将连续值转换成离散值
def is_minor(row):
    if row["Age"] < 18:
        return True
    else:
        return False
minors = titanic.apply(is_minor,axis=1)
def generate_age_label(row):
    age = row["Age"]
    if pd.isnull(age):
        return "unknow"
    elif age < 18:
        return "minor"
    else:
        return "adult"
age_labels = titanic.apply(generate_age_label,axis=1)

### 计算成年人和未成年人获救的关系
titanic['age_labels'] = age_labels
age_group_survival = titanic.pivot_table(index="age_labels",values="Survived")