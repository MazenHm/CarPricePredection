
# 🚗 Car Price Prediction Web App (DecisionTree Model)

This is a machine learning web application that predicts the price of a used car based on its features (brand, model, fuel type, mileage, age, horsepower).

✅ Built with **Flask**, **Scikit-Learn**, **Pandas**  
✅ Deployed with **Decision Tree Regressor** model only  
✅ Login protected (admin login)

---

## 📊 Features

- Predict car prices instantly
- Login/Logout authentication system
- Simple and modern frontend (HTML templates)
- Model retrained and saved via Scikit-Learn Pipeline
- Professionally structured folders

---

## 🧠 ML Pipeline

> **Overall Architecture:**

Data (CSV) ➔ Preprocessing (Scaler + OneHotEncoder) ➔ Train Decision Tree Model ➔ Save Model (.pkl)

> **Web Application Flow:**

User Login ➔ Input Car Details ➔ Model Prediction ➔ Price Display

> **Technical Pipeline Diagram:**

|--- Used Car Dataset (CSV)
    |--- Feature Engineering (car_age, milage, horsepower)
        |--- ColumnTransformer
            |--- Numeric Features (StandardScaler)
            |--- Categorical Features (OneHotEncoder)
                |--- Combined Pipeline
                    |--- Trained DecisionTreeRegressor
                        |--- Save as 'DecisionTree_model.pkl'
                            |--- Flask loads model
                                |--- User Input → Predict Price → Display on Webpage

---

## 🗂 Folder Structure
```
car_price/
├── app.py                   # Flask app
├── README.md
├── requirements.txt
├── used_cars.csv             # Dataset
│
├── models/
│   └── DecisionTree_model.pkl
│
├── static/
│   └── pppp.png              # Static files (images)
│
├── templates/
│   ├── login.html            # Login page
│   └── predict.html          # Prediction page
```
---

## ⚙️ Tech Stack

- **Backend:** Flask
- **Machine Learning:** Scikit-Learn
- **Data Handling:** Pandas, Numpy
- **Frontend:** HTML, Jinja2 templates
- **Deployment:** Localhost (can move to production easily)

---

## 🔐 Login Credentials

| Username | Password |
|:--------:|:--------:|
| admin    | password |

---

## 🚀 How to Run Locally

1. Clone the repository:
```bash
git clone <your-repo-link>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask app:
```bash
python app.py
```

4. Open your browser and visit:
```
http://127.0.0.1:5000/
```

Login using admin credentials, then input car details to predict the price.

---

## 📷 Logo

> Home Page
![Login Page](static/pppp.png)

> Prediction Page
_(you can add your own screenshots)_

---

## 🧹 Notes

- Only the **DecisionTree model** is used for prediction.
- Model and code are compatible with **Scikit-Learn 1.3.0** or latest version.
- Always retrain models if you upgrade Scikit-Learn significantly.

---

## 📜 License

This project is licensed for educational and personal usage.

---

# ✨ Thank You!
