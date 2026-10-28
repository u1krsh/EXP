import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

# Step 1: Load data (example using a sample CSV file)
df = pd.read_csv('Iris.csv')
print("=" * 80)
print("ORIGINAL DATA (First 10 rows)")
print("=" * 80)
print(df.head(10))
print(f"\nOriginal Data Shape: {df.shape}")
print(f"Original Data Info:\n{df.info()}\n")

# Step 2: Data Cleaning
# Drop the Id column and handle missing values
df = df.drop('Id', axis=1)
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
imputer = SimpleImputer(strategy='mean')
df_numeric = pd.DataFrame(imputer.fit_transform(df[numeric_cols]), columns=numeric_cols)
df_imputed = pd.concat([df_numeric, df[['Species']]], axis=1)

print("=" * 80)
print("AFTER PREPROCESSING (First 10 rows)")
print("=" * 80)
print(df_imputed.head(10))
print(f"\nProcessed Data Shape: {df_imputed.shape}")
print(f"Processed Data Info:\n{df_imputed.info()}\n")

# Step 3: Feature Selection
# We want to predict the 'Species' column
X = df_imputed.drop('Species', axis=1)  # Features
y = df_imputed['Species']  # Target

# Step 4: Data Transformation (Standardization and Encoding)
# The Iris dataset is fully numeric, so we only need scaling.

# Step 5: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 6: Create a Pipeline
# Fit preprocessing only on training data through the pipeline to avoid leakage.
pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])

# Step 7: Check model stability with cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(pipeline, X, y, cv=cv)
print(f'Cross-Validation Accuracy: {cv_scores.mean() * 100:.2f}% (+/- {cv_scores.std() * 100:.2f}%)')

# Step 8: Train the Model
pipeline.fit(X_train, y_train)

# Step 9: Evaluate the Model
train_accuracy = pipeline.score(X_train, y_train)
test_accuracy = pipeline.score(X_test, y_test)
print(f'Training Accuracy: {train_accuracy * 100:.2f}%')
print(f'Test Accuracy: {test_accuracy * 100:.2f}%')
