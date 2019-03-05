import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import pandas as pd

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([1, 1, 1, 2, 2, 2])

# Sklearn
sk = LinearDiscriminantAnalysis()
sk.fit(X,y)


# Normal way

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = pd.read_csv('dataset.csv', names=names)
le = LabelEncoder()
#Preprocess
X,y = dataset.iloc[:,:-1].values,dataset.iloc[:,4].values
y = le.fit(y).transform(y)

# D dim mean vectors
np.set_printoptions(precision =4)

mean_vectors = []
for cl in range(1,4):
    mean_vectors.append(np.mean(X[y==cl],axis = 0))
    print('mean class vector {}:{}\n'.format(cl,mean_vectors[cl-1]))

# Scalar matrices 
# within class
S_W = np.zeros((4,4))
for cl,mv in zip(range(1,4),mean_vectors):
    class_sc_mat = np.zeros((4,4))
    for row in X[y==cl]:
        row,mv = row.reshape(4,1),mv.reshape(4,1)
        class_sc_mat += (row-mv).dot((row-mv).T)
    S_W+= class_sc_mat
print('Within class scatter matrix: ',S_W)

#[9 8-0]
print('hello world')