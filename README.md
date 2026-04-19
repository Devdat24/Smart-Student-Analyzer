# 🎓 EduInsight – Smart Student Performance Analyzer

EduInsight is a full-stack machine learning web application designed to analyze and predict student performance using data-driven insights. It leverages multiple ML models to provide comparative performance scores and actionable insights through an interactive web interface.

---

## 🚀 Features

- 📊 **Dual Model Prediction**
  - Logistic Regression
  - Decision Tree Classifier
- 🎯 **Performance Score (1–10 scale)**
- 🔍 **Model Comparison Dashboard**
- 🧠 **Automated Feature Engineering**
  - Study & attendance categories generated dynamically
- 🔐 **User Authentication System**
  - Register / Login / Session handling
- 🗂️ **User History Tracking**
  - Stores past predictions using SQLite
- 📈 **Interactive Visualizations**
  - Charts for model comparison
- 🎨 **Modern UI/UX**
  - Responsive, animated, and clean interface

---

## 🛠️ Tech Stack

| Layer        | Technology Used |
|-------------|----------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Flask (Python) |
| Machine Learning | Scikit-learn |
| Database    | SQLite |
| Visualization | Matplotlib, Chart.js |

---

## 📊 Machine Learning Models

### 1. Logistic Regression
- Used for probability-based classification
- Provides interpretable results
- Works well for linear relationships

### 2. Decision Tree Classifier
- Handles non-linear relationships effectively
- Provides decision-based insights
- Useful for understanding feature importance

---

## 🧠 How It Works

1. User inputs student data via web form  
2. Data is processed and encoded dynamically  
3. Both ML models generate prediction probabilities  
4. Probabilities are converted into a **performance score (1–10)**  
5. Results are displayed along with comparison and stored in database  

---

## 📁 Project Structure
Student_Performance_Project/
│
├── app.py
├── model.py
├── model.pkl
├── users.db
│
├── dataset/
│ └── final_student.csv
│
├── templates/
│ ├── home.html
│ ├── form.html
│ ├── result.html
│ ├── dashboard.html
│ ├── about.html
│ ├── login.html
│ ├── register.html
│ ├── history.html
│
├── static/
│ ├── style.css
│ ├── accuracy.png
│ ├── logistic.png
│ ├── tree.png
│
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/eduinsight.git
cd eduinsight
```
### 2. Install dependencies
pip install -r requirements.txt
### 3. Train the model
python model.py
### 4. Run the application
python app.py
### 5. Open in browser
http://127.0.0.1:5000

### 🔐 Authentication
Users can register and login
Session-based authentication
Prediction history is stored per user

### ⚠️ Important Notes
Dataset preprocessing is handled separately
Feature alignment is maintained using one-hot encoding
Data leakage (e.g., final_exam_score) has been removed for realistic predictions

### 💡 Future Enhancements
🔒 Password hashing & security improvements
📄 Export prediction reports (PDF)
☁️ Deployment on cloud (Render / Railway)
📱 Mobile responsiveness improvements
🤖 Explainable AI (feature importance visualization)

### 🧑‍💻 Author

Devdat Dixit
Computer Engineering Student

### ⭐ Acknowledgements

Scikit-learn Documentation
Flask Documentation
Open-source ML community

### 📌 License

This project is for educational purposes.
