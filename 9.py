import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

# Features (X)
X = pd.DataFrame({
    'Weather': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild'],
})

# Labels (y)
y = pd.Series(['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No'])

# Encode categorical text to numbers
encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X)

# Train the model
model = CategoricalNB()
model.fit(X_encoded, y)

# Test data
test_data = pd.DataFrame({
    'Weather': ['Sunny', 'Rain'],
    'Temperature': ['Cool', 'Mild']
})

# Encode with the SAME encoder, then predict
test_encoded = encoder.transform(test_data)
predictions = model.predict(test_encoded)

print("Predictions:", predictions)