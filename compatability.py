import numpy as np
import math
from naive_bayes import NaiveBayes
from raw_gaus import *


X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

gaussian_fit(NaiveBayes, X, Y)

NaiveBayes()

print(gaussian_predict([[-0.8, -1]]))
# [1]
# clf_pf = GaussianNB()
# clf_pf.partial_fit(X, Y, np.unique(Y))
# GaussianNB()
# print(clf_pf.predict([[-0.8, -1]]))
# # [1]