from flask import Flask, render_template, request, redirect, session
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Load trained model
model_data = pickle.load(open("model.pkl", "rb"))

lr_model = model_data["logistic_model"]
dt_model = model_data["decision_tree_model"]
lr_acc = model_data["lr_accuracy"]
dt_acc = model_data["dt_accuracy"]
features = model_data["features"]


# -------------------- DATABASE SETUP --------------------

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        lr_score REAL,
        dt_score REAL
    )
    """)

    conn.commit()
    conn.close()

init_db()


# -------------------- GRAPH --------------------

def create_accuracy_graph():
    if not os.path.exists("static"):
        os.makedirs("static")

    plt.figure()
    plt.bar(['Logistic', 'Decision Tree'], [lr_acc, dt_acc])
    plt.title("Model Accuracy Comparison")
    plt.ylabel("Accuracy")
    plt.savefig("static/accuracy.png")
    plt.close()

create_accuracy_graph()


# -------------------- ROUTES --------------------

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", lr=lr_acc, dt=dt_acc)


@app.route('/about')
def about():
    return render_template("about.html")


# -------------------- AUTH --------------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user'] = username
            return redirect('/form')
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


# -------------------- FORM --------------------

@app.route('/form')
def form():
    if 'user' not in session:
        return redirect('/login')
    return render_template("form.html")


# -------------------- PREDICTION --------------------

@app.route('/predict', methods=['POST'])
def predict():

    if 'user' not in session:
        return redirect('/login')

    input_df = pd.DataFrame([request.form.to_dict()])

    # Convert numeric values
    for col in input_df.columns:
        try:
            input_df[col] = pd.to_numeric(input_df[col])
        except:
            pass

    # Auto generate categories
    hours = float(input_df["study_hours_per_day"][0])
    if hours < 3:
        input_df["study_hours_category"] = "Low"
    elif hours < 6:
        input_df["study_hours_category"] = "Moderate"
    elif hours < 8:
        input_df["study_hours_category"] = "High"
    else:
        input_df["study_hours_category"] = "Very High"

    attendance = float(input_df["attendance_rate"][0])
    if attendance < 60:
        input_df["attendance_category"] = "Low"
    elif attendance < 80:
        input_df["attendance_category"] = "Good"
    else:
        input_df["attendance_category"] = "Excellent"

    # Encode
    input_df = pd.get_dummies(input_df)

    # Match features
    for col in features:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[features]

    # Debug (optional)
    print("\nINPUT VECTOR:")
    print(input_df.iloc[0])

    # Predict probabilities
    lr_prob = lr_model.predict_proba(input_df)[0][1]
    dt_prob = dt_model.predict_proba(input_df)[0][1]

    # Convert to score
    lr_score = round(lr_prob * 9 + 1, 2)
    dt_score = round(dt_prob * 9 + 1, 2)

    # Save to history
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO history (username, lr_score, dt_score) VALUES (?, ?, ?)",
              (session['user'], lr_score, dt_score))
    conn.commit()
    conn.close()

    return render_template("result.html",
                           lr_score=lr_score,
                           dt_score=dt_score)


# -------------------- HISTORY --------------------

@app.route('/history')
def history():
    if 'user' not in session:
        return redirect('/login')

    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT lr_score, dt_score FROM history WHERE username=?", (session['user'],))
    data = c.fetchall()
    conn.close()

    return render_template("history.html", data=data)


# -------------------- RUN --------------------

if __name__ == "__main__":
    app.run(debug=True)