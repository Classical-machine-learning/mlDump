from sklearn import svm,datasets
from sklearn.model_selection import cross_val_score
from sklearn import linear_model
from sklearn.linear_model import Perceptron
from sklearn.datasets import load_iris
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LogisticRegression


iris = datasets.load_iris()
X,y = iris.data, iris.target

#Linear
print('Linear')
linreg = linear_model.LinearRegression().fit(X,y)
print(linreg.score(X,y))
print(linreg.coef_)

#Logistic
print('\nLogistic')
logreg = LogisticRegression(random_state = 0,solver = 'lbfgs',multi_class='multinomial').fit(X,y)
print(logreg.coef_)
print(logreg.score(X,y))

#Polynomial
print('\nPolynomial/Perceptron')
poly = PolynomialFeatures(degree = 3).fit_transform(X)
#print(poly)
perc = Perceptron(fit_intercept= False,max_iter = 20,tol = None,shuffle = False).fit(poly,y)
print(perc.score(poly,y))

#Ridge
print('\nRidge')
rireg = linear_model.BayesianRidge()
rireg.fit(X,y)
print(rireg.coef_)
print(rireg.score(X,y))

#Lasso 
print('\nLasso')
lass = linear_model.Lasso(alpha =0.1)
lass.fit(X,y)
print(lass.coef_)
print(lass.score(X,y))

#ElasticNet
print('\nElasticNet')
elas = ElasticNet(random_state=0)
elas.fit(X,y)
print(elas.coef_)
print(elas.score(X,y))

#Robust 
print('\nRobust')
rb = linear_model.RANSACRegressor().fit(X,y)
print(rb.score(X,y))
