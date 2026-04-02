# 🎓 Student Performance Analytics & Prediction System

## 📌 Overview

The **Student Performance Analytics & Prediction System** is a machine learning-based web application that predicts a student's final academic performance based on key input parameters such as study time, absences, and internal assessment scores.

This project demonstrates an **end-to-end data science pipeline**, including data preprocessing, model training, backend integration, and database storage, deployed through a dynamic web interface using Flask.

---

## 🚀 Features

* 📊 Predicts final student performance (G3 score)
* 🧠 Machine Learning model using Linear Regression
* 🌐 Dynamic web application built with Flask
* 🗄️ SQLite database integration for storing predictions
* 🎨 Multi-page UI (Home, Prediction, About)
* 📈 Clean and structured dataset preprocessing

---

## 🧠 Tech Stack

### 🔹 Frontend

* HTML5
* CSS3
* Bootstrap (optional enhancements)

### 🔹 Backend

* Python
* Flask

### 🔹 Machine Learning

* Pandas
* NumPy
* Scikit-learn

### 🔹 Database

* SQLite

---

## 📊 Dataset

* Source: Kaggle – Student Performance Dataset
* Attributes used:

  * `studytime` – Weekly study duration (1–4 scale)
  * `absences` – Number of school absences
  * `G1` – First internal marks
  * `G2` – Second internal marks
  * `G3` – Final marks (target variable)

---

## ⚙️ How It Works

1. User inputs student details via web form
2. Flask backend processes input data
3. Data is passed to trained Linear Regression model
4. Model predicts final marks (G3)
5. Prediction is displayed to user
6. Input + prediction stored in SQLite database

---

## 🔄 Project Workflow

```
Dataset → Preprocessing → Model Training → Flask Backend → Prediction → Database Storage → UI Display
```

---

## 🧹 Data Preprocessing

* Loaded dataset using Pandas
* Checked for missing values
* Selected relevant features
* Converted categorical data (if required)
* Saved cleaned dataset for training

---

## 🤖 Machine Learning Model

### Model Used:

**Linear Regression**

### Why Linear Regression?

* Suitable for continuous output prediction
* Simple and interpretable
* Efficient for small datasets
* Provides fast and reliable results

---

## 📂 Project Structure

```
student-performance-project/
│
├── app.py
├── model.py
├── database.py
├── model.pkl
├── students.db
│
├── dataset/
│   └── cleaned_student.csv
│
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── about.html
│   ├── dashboard.html
│
├── static/
│   └── style.css
```

---

## ▶️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/your-username/student-performance-project.git
cd student-performance-project
```

### 2. Install Dependencies

```
pip install flask pandas scikit-learn numpy
```

### 3. Train Model

```
python model.py
```

### 4. Create Database

```
python database.py
```

### 5. Run Application

```
python app.py
```

### 6. Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📈 Future Enhancements

* Add data visualization dashboard
* Implement classification (pass/fail prediction)
* Improve UI with advanced frameworks
* Deploy on cloud (AWS / Heroku)
* Use advanced ML models (Random Forest, XGBoost)

---

## 🎯 Learning Outcomes

* End-to-end ML project implementation
* Data preprocessing and feature selection
* Model training and evaluation
* Backend integration using Flask
* Database handling with SQLite

---

## 👨‍💻 Author

**Devdat Dixit**

---

## 📜 License

This project is for academic and educational purposes.
