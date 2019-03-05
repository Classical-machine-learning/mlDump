from sklearn import svm,datasets
iris = datasets.load_iris()
X,y = iris.data, iris.target

print("SVC")
sv = svm.SVC(gamma='scale',decision_function_shape='ovo').fit(X,y)
print(sv.score(X,y))

print("\nLinear SVM")
svl = svm.LinearSVC().fit(X,y)
print(svl.score(X,y))

print("\nSVR")
sv2 = svm.SVR().fit(X,y)
print(sv2.score(X,y))

print("\nLinear SVR")
svl2 = svm.LinearSVR().fit(X,y)
print(svl2.score(X,y))
