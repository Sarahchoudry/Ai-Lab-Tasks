import pandas as pd
import numpy as np
import pickle
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Step 1: Load the Diabetes Dataset
df = pd.read_csv("diabetes.csv")  # Replace with the correct path to your dataset

# Step 2: Basic Data Inspection
print(f"Number of Rows: {df.shape[0]} \nNumber of Columns: {df.shape[1]}")
print(df.head(2))
print(df.tail(2))
print(df.describe())
print(df.info())

# Step 3: Check for missing values
print("-- Number of Null Values in Data --")
print(df.isnull().sum())

# Step 4: Handling Missing Values
# Replace zeroes or missing values in critical columns with the median (e.g., Glucose, BMI, etc.)
columns_with_zeroes = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Age']
for col in columns_with_zeroes:
    df[col] = df[col].replace(0, df[col].median())

# Step 5: Feature-Target Split
X = df.drop('Outcome', axis=1)  # Features (excluding the target variable 'Outcome')
y = df['Outcome']  # Target variable

# Step 6: Train-Test Split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Feature Scaling (Standardization for better performance with SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 8: Train the SVM Classifier
svm_classifier = SVC(kernel='linear')  # You can try other kernels like 'rbf', 'poly'
svm_classifier.fit(X_train_scaled, y_train)

# Step 9: Make Predictions
y_pred = svm_classifier.predict(X_test_scaled)

# Step 10: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print(f"-- Model Accuracy Score: {accuracy:.3f}")

# You can print the classification report for detailed evaluation
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

# Step 11: Save the Model (optional)
pickle.dump(svm_classifier, open('svm_diabetes_model.pkl', 'wb'))


