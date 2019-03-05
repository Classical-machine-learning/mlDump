# README

This code demonstrates some of the various types of regressions that are present.
Namely:

1) Linear regression(Also called frequentist):
- Relation between a Dependant variable (Y) and an independent variable (X) using a  best fit line. 
- Multiple linear regression has more than 1 independent variable
- Must be a linear relationship
- Take care of outliers

2) Logistic Regression
- Probability of success and failure
- Binomial distribution
- Classification problems
- Requires large dataset

3) Polynomial regression
- Line of best fit is a polynomial
- Over fitting is possible

4) StepWise regression(no code)
- Multiple independent variables
- Automatic selection of variables
- Adds and removes predictors as needed
- Forward selection and backwards elimination
- Max prediction with minimum variables

5) Ridge Regression
- When independent variables are highly correlated
- Degree of bias is added to reduce errors
- No feature selection

6) Lasso regression
- Least absolute shrinkage and selection operator
- Reduces variability and improves accuracy of Linear regression
- Helps in feature selection
- If group of predictors are related, only one is picked, the rest become zero

7) ElasticNet regression
- Hybrid of ridge and lasso
- Useful when multiple correlated feature
- Lasso will pick one, ElasticNet will pick both
- No limits on no of selected variables
- Can have double shrinkage

8) Bayesian Linear Regression(implemented in ridge)
- Linear regression using probability distributions rather than point estimates
- Response in not a single value but obtained from a probability distribution
- Posterior distribution for the model parameters
- As we gather more evidence, our model becomes less wrong

9) Robust Regression
- Alternative to OLS
- Data is contaminated with outliers or influencial observstions
- Can also be used to detect influential observations


