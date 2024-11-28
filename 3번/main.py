import pandas as pd
from sklearn.preprocessing import StandardScaler

filename = "./data/08_pima-indians-diabetes.data.csv"

column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = pd.read_csv(filename, names=column_names)

array = data.values
print(array, "\n array 변수의 행렬 shape:", array.shape)

X = array[:, 0:8]
print(X, "\nX shape is ", X.shape)
print("----------------------")
Y = array[:, 8]
print(Y, "\nY shape is ", Y.shape)

scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)

print(rescaledX)