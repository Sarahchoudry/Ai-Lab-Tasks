import pandas as pd
import numpy as np
import pickle
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv("diabetes.csv")  
print(f"Number of Rows: {df.shape[0]} \nNumber of Columns: {df.shape[1]}")
print(df.head(2))
print(df.tail(2))
print(df.describe())
print(df.info())

print("-- Number of Null Values in Data --")
print(df.isnull().sum())

columns_with_zeroes = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Age']
for col in columns_with_zeroes:
    df[col] = df[col].replace(0, df[col].median())


X = df.drop('Outcome', axis=1)  
y = df['Outcome']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svm_classifier = SVC(kernel='linear') 
svm_classifier.fit(X_train_scaled, y_train)

y_pred = svm_classifier.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
print(f"-- Model Accuracy Score: {accuracy:.3f}")


from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


pickle.dump(svm_classifier, open('svm_diabetes_model.pkl', 'wb'))


