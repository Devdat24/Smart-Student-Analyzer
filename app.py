from flask import Flask, render_template, request
import pickle
import numpy as np
import sqlite3

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# DB connection
conn = sqlite3.connect('students.db', check_same_thread=False)
cursor = conn.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict-page')
def predict_page():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    studytime = int(request.form['studytime'])
    absences = int(request.form['absences'])
    G1 = int(request.form['G1'])
    G2 = int(request.form['G2'])

    # Example input (simplified)
    input_data = np.array([[studytime, absences, G1, G2]])

    prediction = model.predict(input_data)[0]

    # Store in DB
    cursor.execute(
    "INSERT INTO students (studytime, absences, G1, G2, predicted_G3) VALUES (?,?,?,?,?)",
    (studytime, absences, G1, G2, prediction)
)
    conn.commit()
    return render_template('dashboard.html', prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)