# README

1) Classification tree:
- Many trees below can be used for classification

2) Random forest:
-Meta estimator
- Fits a number of classifying decision trees on various sub samples of the data
- uses averaging to improve accuracy
- Control over fitting


3) Decision tree: 
- Used for classification and regression
- Learning simple decision rules inferred from data features
- Requires little data prep
- Numerical and categorical data
- Multi output problems
- Can end up with biased trees

4) Regression tree:
- Mostly same as 3

5) SVM (Support Vector Machines)
- Supervised
- Classification, Regression, Outlier detection
- Effective in high dimensions
- Uses support vectors
- Custom kernels can be used
- No probability estimates
- SVC and NuSVC : One against One
- LinearSVC : One vs rest

6) SVR (Support Vector Regression)
- Extending classification to solve regression probs
- depends on only a subset of training data
- SVR, NuSVR, LinearSVR. 
- LinearSVR is faster but only uses linear kernels
- NuSVR is differnt from both.
