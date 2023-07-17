import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import pickle

# Load the model from the pickle file
with open('trained_model\stroke_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Prepare the test data
test_data = pd.DataFrame([[55, 1, 0, 'Yes', 'Private', 120.5, 25.5, 'formerly smoked']],
                         columns=['age', 'hypertension', 'heart_disease', 'ever_married', 'work_type',
                                  'avg_glucose_level', 'bmi', 'smoking_status'])
# Handle missing values
test_data['bmi'].fillna(test_data['bmi'].mean(), inplace=True)

# Perform one-hot encoding for categorical variables
categorical_features = ['work_type', 'smoking_status']
test_data_encoded = pd.get_dummies(test_data, columns=categorical_features)
# Preprocess the features using standard scaling
scaler = StandardScaler()
test_data_scaled = scaler.transform(test_data_encoded)
# Make predictions on the test data
predictions = model.predict(test_data_scaled)

# Print the predictions
print("Predicted Stroke:", predictions[0])
