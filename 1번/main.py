import pandas as pd
dir = "./data/"
filename = "08_pima-indians-diabetes.data.csv"
filepath = dir + filename

data_columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv(filepath, names=data_columns)

print(data.head(5))