from flask import render_template, flash, redirect, url_for
from app import app
from .form import LoanPredictionForm
import joblib
import numpy as np

model_filename = "app/models/Random forest joblib.h5"
model = joblib.load(model_filename)

@app.route("/")
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = LoanPredictionForm()
    if form.validate_on_submit():
        try:
            # Collect data from the form
            data = np.array([
                form.gender.data,
                form.married.data,
                form.dependents.data,
                form.education.data,
                form.self_employed.data,
                form.applicant_income.data,
                form.coapplicant_income.data,
                form.loan_amount.data,
                form.loan_amount_term.data,
                form.credit_history.data,
                form.property_area.data
            ]).reshape(1, -1)

            # Preprocess data
            data = preprocess_data(data)

            # Make prediction
            prediction = model.predict(data)
            prediction_text = 'Loan Approved' if prediction == 1 else 'Loan Rejected'
            flash(prediction_text, 'success')
            return redirect(url_for('predict'))
        
        except Exception as e:
            flash(f'An error occurred.', 'danger')
            return redirect(url_for('predict'))
    
    return render_template('loan.html', title='Loan Prediction', form=form)

def preprocess_data(data):
    # Convert categorical data to numerical values based on your encoding
    gender_map = {'Male': 1, 'Female': 0}
    married_map = {'Yes': 1, 'No': 0}
    dependents_map = {'0': 0, '1': 1, '2': 2, '3+': 3}
    education_map = {'Graduate': 1, 'Not Graduate': 0}
    self_employed_map = {'Yes': 1, 'No': 0}
    property_area_map = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}

    data[0][0] = gender_map[data[0][0]]
    data[0][1] = married_map[data[0][1]]
    data[0][2] = dependents_map[data[0][2]]
    data[0][3] = education_map[data[0][3]]
    data[0][4] = self_employed_map[data[0][4]]
    data[0][10] = property_area_map[data[0][10]]

    # Convert the data array to floats
    data = data.astype(float)
    
    return data
