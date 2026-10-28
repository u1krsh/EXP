import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 2: Reading the Dataset
df = pd.read_csv('bottle.csv')
df_binary = df[['Salnty', 'T_degC']]  # Taking only the selected two attributes from the dataset
df_binary.columns = ['Sal', 'Temp']  # Renaming the columns for easier writing of the code
df_binary.head()  # Displaying only the 1st rows along with the column names

# Step 3: Data Cleaning
# Eliminating NaN or missing input numbers
df_binary.fillna(method='ffill', inplace=True)

# Step 4: Training Our Model
# Separating the data into independent and dependent variables
# Converting each dataframe into a numpy array
# since each dataframe contains only one column
X = np.array(df_binary['Sal']).reshape(-1, 1)
y = np.array(df_binary['Temp']).reshape(-1, 1)

df_binary.dropna(inplace=True)  # Dropping any rows with NaN values

# Splitting the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

regr = LinearRegression()
regr.fit(X_train, y_train)
print(regr.score(X_test, y_test))
print(df)

# Step 5: Exploring Our Results
y_pred = regr.predict(X_test)
plt.scatter(X_test, y_test, color='b')
plt.plot(X_test, y_pred, color='k')
plt.show()  # Data scatter of predicted values