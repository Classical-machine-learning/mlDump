
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.preprocessing import LabelEncoder
import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = pd.read_csv('dataset.csv', names=names)
le = LabelEncoder()
#Preprocess
X,y = dataset.iloc[:,:-1].values,dataset.iloc[:,4].values
y = le.fit(y).transform(y)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = .2)
# Standard scaler
scaler = MinMaxScaler(feature_range=(0,1))
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#KNN
classifier = KMeans(n_clusters = 2,max_iter = 600,algorithm = 'auto')
classifier.fit(X_train,y_train)

# Pred
y_pred = classifier.predict(X_test)

#Evaluation

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
