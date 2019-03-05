import pandas as pd
import scipy
import numpy as np
from sklearn.preprocessing import MinMaxScaler

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('dataset.csv',names = names)
arr = data.values
#print(arr)
X = arr[:,0:8]
Y = arr[:,8]
#print(X,Y)

scaler = MinMaxScaler(feature_range = (0,1))
newX = scaler.fit_transform(X)
np.set_printoptions(precision =3)
print(newX)
