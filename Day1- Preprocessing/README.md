# README
1) Binarize.py - Binerization transforms  data using a binary threshold.  every value which is above the threshold is marked as 1 and all which are equal to or below that is marked as 0.
These are useful when there are many probabilities
Useful also for feature engineering.

2) LabelEncoding.py - If  our dataset has other features which are non-numerical that is,  they are strings. They can be converted into  numerical features using label encoding.

3) Normalize.py - Normalization is rescaling each row to havea. length of 1(unit norm)
Useful for sparse datasets (many 0 in matrix)
Useful for NNs and distance measure algos.

4) OneHot.py- The problem of label  encoding is that it assumes that the higher the categorical value, the better is the category.  in one Hot encoding,  binarization of the categories is done.

5) Rescale.py = Normalization - attributes are rescaled into the range between 0 and 1.
Useful for algorithms that weight inputs like regression, NN and distance measure algos.

6) Standardize.py - Rescaling is used for attributes with a Gaussian dist and differing means and std.devs to a distribution with mean = 0, stddev =1
Useful for linear regression. logistic regression and linear discriminate analysis.

