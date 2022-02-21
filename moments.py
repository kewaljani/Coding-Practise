import numpy as np

#Consider three variables call them x_0, x_1, x_2 with 5 observations each; 
# represented as a matrix of dim 3 x 5

X = np.array([ [0.1, 0.3, 0.4, 0.8, 0.9],
               [3.2, 2.4, 2.4, 0.1, 5.5]
             ])



# to calculate correlation coefficient: 
# https://en.wikipedia.org/wiki/Correlation
print("correlation matrix:") 
print(np.corrcoef(X))

# to calc. covaraince matrix: 
# print("covariance matrix:")
print(np.cov(X))

# calc. variance of X of each var: x_0, x_1, x_2
print("variance for each var:")
print(np.var(X))

X[0][0] = 2*X[0]
print(X)