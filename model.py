import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv('dataset/cleaned_student.csv')

# Select ONLY required columns
df = df[['studytime', 'absences', 'G1', 'G2', 'G3']]

# Features & Target
X = df[['studytime', 'absences', 'G1', 'G2']]
y = df['G3']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained successfully!")