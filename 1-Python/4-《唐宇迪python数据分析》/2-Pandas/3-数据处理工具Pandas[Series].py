## Series 相当于DataFrame的某一行或某一列
import pandas as pd
import numpy as np

titanic = pd.read_csv('../train.csv')
fares = titanic["Fare"]
print( type(fares) )    # <class 'pandas.core.series.Series'>
print( fares[0:5] )

