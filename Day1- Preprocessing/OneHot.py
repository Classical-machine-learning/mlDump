
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

data_orig=pd.read_csv('dataset2.csv')

enc=OneHotEncoder(handle_unknown='ignore')

names = [['Male', 1], ['Female', 3], ['Female', 2]]
enc.fit(names)

print(enc.categories_)
print(enc.transform(names).toarray())
print(enc.get_feature_names())
