import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
dataset = pd.read_csv("diabetes.csv")
x = dataset.iloc[:, [4, 7]].values
y = dataset.iloc[:, 8].values
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25, random_state=0)
sc_x = StandardScaler()
xtrain = sc_x.fit_transform(xtrain)
xtest = sc_x.transform(xtest)
print(xtrain[0:10, :])
classifier = LogisticRegression(random_state=0)
classifier.fit(xtrain, ytrain)
y_pred = classifier.predict(xtest)
accuracy = accuracy_score(ytest, y_pred)
precision = precision_score(ytest, y_pred)
recall = recall_score(ytest, y_pred)
f1 = f1_score(ytest, y_pred)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)