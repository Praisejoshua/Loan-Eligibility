from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange

class LoanPredictionForm(FlaskForm):
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    married = SelectField('Married', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    dependents = SelectField('Dependents', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3+', '3+')], validators=[DataRequired()])
    education = SelectField('Education', choices=[('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')], validators=[DataRequired()])
    self_employed = SelectField('Self Employed', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    applicant_income = FloatField('Applicant Income', validators=[DataRequired(), NumberRange(min=0)],  render_kw={"placeholder" : "Enter Number"})
    coapplicant_income = FloatField('Coapplicant Income', validators=[DataRequired(), NumberRange(min=0)], render_kw={"placeholder" : "Enter Number"})
    loan_amount = FloatField('Loan Amount', validators=[DataRequired(), NumberRange(min=0)],  render_kw={"placeholder" : "Enter Number"})
    loan_amount_term = FloatField('Loan Amount Term', validators=[DataRequired(), NumberRange(min=1)],  render_kw={"placeholder" : "Enter Number"})
    credit_history = SelectField('Credit History', choices=[('0', 'No'), ('1', 'Yes')], validators=[DataRequired()])
    property_area = SelectField('Property Area', choices=[('Urban', 'Urban'), ('Semiurban', 'Semiurban'), ('Rural', 'Rural')], validators=[DataRequired()])
    submit = SubmitField('Predict')
