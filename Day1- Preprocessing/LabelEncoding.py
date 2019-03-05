
from sklearn.preprocessing import LabelEncoder
import pandas as pd

data_orig=pd.read_csv('dataset2.csv')

le=LabelEncoder()

names2 = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

names=le.fit(names2)
print(list(names.classes_))
names3 =le.transform(names2)
print(names3)
