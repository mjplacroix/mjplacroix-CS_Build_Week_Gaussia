from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
print(X_train.shape, y_test.shape)
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
accuracy = round((1 - (y_test != y_pred).sum() / X_test.shape[0]) * 100, 2)
print(f"Accuracy: {accuracy}%")
# Number of mislabeled points out of a total 75 points : 4