

import pandas as pd
import scipy
import numpy as np
from sklearn.preprocessing import Binarizer

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('dataset.csv',names = names)
arr = data.values

#print(arr)
X = arr[:,0:8]
Y = arr[:,8]
#print(X,Y)

bina = Binarizer(threshold = 0.0).fit(X)
newX = bina.transform(X)
np.set_printoptions(precision=3)
print(newX[0:5,:])
