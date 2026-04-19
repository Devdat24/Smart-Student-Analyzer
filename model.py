# Import required libraries
import pandas as pd
import numpy as np
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
file_path = "dataset/final_student.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Dataset not found at {file_path}")

df = pd.read_csv(file_path)

print("\nColumns in dataset:", df.columns)

# Set target column
target_col = "pass_fail"

if target_col not in df.columns:
    raise Exception(f"{target_col} not found in dataset")

# Drop unnecessary and leakage columns
drop_cols = [
    "student_id",
    "grade_category",
    "final_exam_score"   # 🔥 REMOVE LEAKAGE
]

df = df.drop(columns=[col for col in drop_cols if col in df.columns])

# Separate target variable
y = df[target_col]

# Convert target to numeric if needed
if y.dtype == "object":
    y = y.map({"Pass": 1, "Fail": 0})

# Check for invalid values
if y.isnull().any():
    raise ValueError("Unexpected values found in target column")

# Prepare feature variables
X = df.drop(columns=[target_col])

# Encode categorical features
X = pd.get_dummies(X, drop_first=True)

# Handle missing values
X.fillna(X.mean(), inplace=True)

# Verify final data
print("\nFinal Features Used:", len(X.columns))

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize models
lr_model = LogisticRegression(max_iter=1000)
dt_model = DecisionTreeClassifier(max_depth=5)

# Train models
lr_model.fit(X_train, y_train)
dt_model.fit(X_train, y_train)

# Make predictions
lr_pred = lr_model.predict(X_test)
dt_pred = dt_model.predict(X_test)

# Evaluate models
lr_acc = accuracy_score(y_test, lr_pred)
dt_acc = accuracy_score(y_test, dt_pred)

print("\nModel Performance:")
print(f"Logistic Regression Accuracy: {lr_acc:.4f}")
print(f"Decision Tree Accuracy: {dt_acc:.4f}")

# Save models and metadata
model_data = {
    "logistic_model": lr_model,
    "decision_tree_model": dt_model,
    "lr_accuracy": lr_acc,
    "dt_accuracy": dt_acc,
    "features": list(X.columns)
}

with open("model.pkl", "wb") as f:
    pickle.dump(model_data, f)

print("\n Models trained and saved successfully as model.pkl")