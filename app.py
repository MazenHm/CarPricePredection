from flask import Flask, render_template, request, redirect, session
import joblib
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = 'supersecretkey'

MODELS = {
    "LinearRegression": "LinearRegression_model.pkl",
    "RidgeRegression": "RidgeRegression_model.pkl",
    "DecisionTree": "DecisionTree_model.pkl"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            return redirect('/predict')
        else:
            error = 'Invalid Credentials'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if not session.get('logged_in'):
        return redirect('/')

    predictions = {}
    error = None

    if request.method == 'POST':
        try:
            brand = request.form['brand']
            car_model = request.form['car_model']
            fuel_type = request.form['fuel_type']
            milage = float(request.form['milage'])
            model_year = int(request.form['model_year'])
            horsepower = float(request.form['horsepower'])

            car_age = 2025 - model_year
            input_data = pd.DataFrame([{
                'brand': brand,
                'model': car_model,
                'fuel_type': fuel_type,
                'milage': milage,
                'car_age': car_age,
                'horsepower': horsepower
            }])

            for model_name, file in MODELS.items():
                model_path = os.path.join(os.path.dirname(__file__), file)
                model = joblib.load(model_path)
                predictions[model_name] = round(model.predict(input_data)[0], 2)

        except Exception as e:
            error = str(e)

    return render_template('predict.html', models=MODELS.keys(), predictions=predictions, error=error)

if __name__ == '__main__':
    app.run(debug=True)
