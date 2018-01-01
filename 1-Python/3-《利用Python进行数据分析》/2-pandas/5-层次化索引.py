## 层次化索引是pandas的一项重要功能，使你能在一个轴上拥有多个（两个以上）索引级别。
## 抽象就是使你能以低维度形式处理高维度数据。
## 如创建一个Series 并用一个由列表或数组组成的列表作为索引。

import numpy as np
from pandas import Series,DataFrame
import pandas as pd

a1 = Series(np.random.rand(10),index=[['a','a','a','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])

### 暂时先没看完

