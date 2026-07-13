# 🚢 Titanic Survival Predictor

A Machine Learning web application that predicts whether a passenger would have survived the Titanic disaster based on passenger information. The project is built using **Flask**, **Scikit-learn**, **HTML**, **CSS**, and **Bootstrap**, and is trained on the famous **Kaggle Titanic Dataset**.

---

## 🌐 Live Demo

🔗 **Live Website:** https://your-render-link.onrender.com

---

## 📌 Features

- 🚢 Predicts Titanic passenger survival
- 🤖 Machine Learning model (Logistic Regression)
- 📊 Displays survival probability
- 💻 Responsive and modern light-themed UI
- ⚡ Fast prediction using Flask backend
- 📱 Mobile-friendly design

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

### Backend
- Flask

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Deployment
- Render

---

## 📂 Project Structure

```
Titanic-Survival-Predictor/
│
├── app.py
├── requirements.txt
├── Procfile
├── README.md
│
├── model/
│   ├── logistic_model.pkl
│   └── feature_columns.pkl
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── templates/
│   └── index.html
│
└── notebook/
    └── Titanic_Model.ipynb
```

---

## 📊 Dataset

This project uses the **Titanic Dataset** from Kaggle.

Dataset includes features such as:

- Passenger Class
- Gender
- Age
- Fare
- Number of Siblings/Spouses
- Number of Parents/Children
- Embarked Port
- Cabin Availability
- Passenger Title

---

## ⚙️ Feature Engineering

The following features were engineered before training the model:

- Family Size
- Is Alone
- Has Cabin
- Passenger Title Extraction
- One-Hot Encoding
- Missing Value Handling

---

## 🤖 Machine Learning Model

**Algorithm Used**

- Logistic Regression

The model predicts:

- ✅ Likely to Survive
- ❌ Not Likely to Survive

along with the **Survival Probability (%)**.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Titanic-Survival-Predictor.git
```

Go to the project folder:

```bash
cd Titanic-Survival-Predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page

_Add a screenshot here_

### Prediction Result

_Add a screenshot here_

---

## 📈 Future Improvements

- XGBoost and Random Forest comparison
- Interactive charts and visualizations
- Dark Mode
- Passenger history dashboard
- Explainable AI (SHAP)

---

## 👩‍💻 Author

**Deeva Jain**

- GitHub: https://github.com/Deeva2601
- LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ If you like this project

Please consider giving it a **Star ⭐** on GitHub.

---

## 📜 License

This project is developed for educational and portfolio purposes.
