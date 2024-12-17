#1
import pandas as pd
from Tools.scripts.make_ctype import values
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from  sklearn.metrics import accuracy_score

from main import filename, scaler

filename = "./data/1_pima.csv"

column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = pd.read_csv('./data/1_pima.csv', names=column_names)

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

y_pred_binary = (y_pred > 0.5).astype(int)
print(y_pred_binary)

accuracy = accuracy_score(y_test, y_pred_binary)

print("---------------------")
print("Actual Values:", y_test)
print("Predicted Values:", y_pred_binary)
print("---------------------")
print("Accuracy:", accuracy)

#2
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

filename = "./data/1_pima.csv"

column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = pd.read_csv(filename, names=column_names)

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=41)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

accuracy = accuracy_score(y_test, y_pred_binary)

print("---------------------")
print("Actual Values:", y_test)
print("Predicted Values:", y_pred_binary)
print("---------------------")
print("Accuracy:", accuracy)

#3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

filename = "./data/1_pima.csv"

column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = pd.read_csv(filename, names=column_names)

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=41)

model = DecisionTreeClassifier(max_depth=1000, min_samples_split=60, min_samples_leaf=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)

print("---------------------")
print("Actual Values:", y_test)
print("Predicted Values:", y_pred)
print("---------------------")
print("Accuracy:", accuracy)