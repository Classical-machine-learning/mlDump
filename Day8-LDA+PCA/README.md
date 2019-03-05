# README

# Note: TO COMPLETE

## LDA(Linear Discriminant Analysis)
- dimentionality reduction
- pre processing
- Project a feature space onto a smaller subspace k 
- Maintains discriminatory info.
- Supervised
- Computes the linear discriminants
- Maximizes component axes for class separation
- Assumes normal distribution

### Steps for LDA

1) Computing d- dimensoinal mean vectors
2) Compute scatter matrices: Sw = Sigma(Si,i=1,c)
	Si = Sigma((x-mi)(x-mi)^T,x£Di,n)
	mi is mean vector

	Sb = Sigma(N,(mi-m)(mi-m)^T,i=1,c)
3) Solve generalized eigenvalue problem for Sw^-1Sb
4) Select linear discriminants for new feature subspace
	1) Sort eigenvectors by decreasing eigenvalues
	2) Choosing k eigenvectors with largest eigenvalues
5) Transforming samples onto new subspace
	Y = X*W


## PCA
- Directions that maximize variance 
- Projecting entire dataset without class labels onto a different subspace
- Unsupervised

### Steps to PCA
1) Take the whole dataset and ignore class labels
2) Compute d dimensional mean vector
3) Compute scatter matrix
4) Compute eigenvectors and eigenvalues
	Check using Sigma*v = Lambda*v
5) Sort eigenvectors by decreasing eigenvalues
6) Choose k eigenvectors with largest eigenvalues
7) Transform samples onto new subspace

