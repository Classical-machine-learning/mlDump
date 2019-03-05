
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = pd.read_csv('dataset.csv', names=names)

#Preprocess
X,y = dataset.iloc[:,:-1].values,dataset.iloc[:,4].values

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = .2)
# Standard scaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#KNN
classifier = KNeighborsClassifier(n_neighbors = 5)
classifier.fit(X_train,y_train)

# Pred
y_pred = classifier.predict(X_test)

#Evaluation

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
