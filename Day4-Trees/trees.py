from sklearn import tree
from sklearn import datasets
import graphviz
from sklearn.ensemble import RandomForestRegressor

iris = datasets.load_iris()
X,y = iris.data, iris.target

print("Decision Tree")
dectree = tree.DecisionTreeClassifier().fit(X,y)
trr = tree.export_graphviz(dectree,out_file=None)
print(dectree.score(X,y))
graph = graphviz.Source(trr)
graph.render("iris")

print("\nRandom Forest")
ranf = RandomForestRegressor(n_estimators = 100,random_state=0).fit(X,y)
print(ranf.score(X,y))

print("\nRegression Tree")
dectree2 = tree.DecisionTreeRegressor().fit(X,y)
trr2 = tree.export_graphviz(dectree2,out_file=None)
print(dectree2.score(X,y))
graph = graphviz.Source(trr2)
graph.render("iris2")
