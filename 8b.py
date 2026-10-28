import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_boston

# Load the Iris dataset
iris = load_iris()
iris_data = iris.data
iris_feature_names = iris.feature_names

# Convert Iris data to a pandas DataFrame
iris_df = pd.DataFrame(iris_data, columns=iris_feature_names)

# Calculate correlation matrix for Iris dataset
iris_corr_matrix = iris_df.corr()

# Print correlation matrix for Iris dataset
print("Correlation Matrix for Iris dataset:")
print(iris_corr_matrix)
print()

# Load the Boston Housing dataset
boston = load_boston()
boston_data = boston.data
boston_feature_names = boston.feature_names

# Convert Boston Housing data to a pandas DataFrame
boston_df = pd.DataFrame(boston_data, columns=boston_feature_names)

# Calculate correlation matrix for Boston Housing dataset
boston_corr_matrix = boston_df.corr()

# Print correlation matrix for Boston Housing dataset
print("Correlation Matrix for Boston Housing dataset:")
print(boston_corr_matrix)
print()

# Calculate pairwise correlation between two features in the Boston Housing dataset
crim_corr = boston_df['CRIM'].corr(boston_df['TAX'])
print("Correlation between 'CRIM' and 'TAX' in Boston Housing dataset:", crim_corr)

