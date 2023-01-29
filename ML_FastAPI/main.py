from joblib import load
from fastapi import FastAPI, Query
import numpy as np
from pydantic import BaseModel

oh_encoder = load('joblib_files/oh_encoder.joblib')
std_scaler = load('joblib_files/std_scaler.joblib')
model = load('joblib_files/model_file.joblib')

app = FastAPI()

@app.get("/")
def read_root():
    return {"Description":[{"By": "Yash Jain"}, {"Project": "Credit Risk Prediction"}, {"Description": "This is a credit risk prediction model which predicts whether user will be in high risk or low risk category."},{"Api":"http://127.0.0.1:8000/predict"},{"Contact": "yashj133.yj@gmail.com"}]}

class Item(BaseModel):
    Gender: str = Query(...,description="['male' 'female']")
    Marital_status: str = Query(...,description="['single' 'divorced/separated/married' 'divorced/separated' 'married/widowed']")
    Housing: str = Query(...,description="['own' 'for free' 'rent']")
    Employment_status: str = Query(...,description="['unemployed' 'skilled employee' 'management/ self-employed' 'unskilled - resident' 'unskilled - non-resident']")
    Has_been_employed_for_at_least: str = Query(...,description="['7 years' '1 year' '4 years' '0 year']")
    Has_been_employed_for_at_most: str = Query(...,description="['4 years' '7 years' '0 year' '1 year']")
    Savings_account_balance: str = Query(...,description="['Low' 'High' 'Medium' 'Very high']")
    Purpose: str = Query(...,description="['electronic equipment' 'education' 'FF&E' 'new vehicle' 'used vehicle' 'business' 'domestic appliances' 'repair costs' 'career development']")
    Property: str = Query(...,description="['skilled employee / official' 'unskilled - resident''management / self-employed / highly qualified employee / officer' 'unemployed / unskilled - non-resident']")
    Loan_history: str = Query(...,description="['critical/pending loans at other banks' 'existing loans paid back duly till now' 'delay in paying off loans in the past' 'no loans taken/all loans paid back duly' 'all loans at this bank paid back duly']")
    Months_loan_taken_for: int = Query(...,description="Number of months loan taken for")
    Principal_loan_amount: int = Query(...,description="Principal loan amount")
    Primary_applicant_age_in_years: int = Query(...,description="Primary applicant age in years")
    EMI_rate_in_percentage_of_disposable_income: int = Query(...,description="EMI rate in percentage of disposable income")
    Has_coapplicant: int = Query(...,description="Has coapplicant")
    Has_guarantor: int = Query(...,description="Has guarantor")
    Number_of_existing_loans_at_this_bank: int = Query(...,description="Number of existing loans at this bank")
    Number_of_dependents: int = Query(...,description="Number of dependents")
    Years_at_current_residence: int = Query(...,description="Years at current residence")
    Foreign_worker: int = Query(...,description="Foreign worker")
    
@app.post("/predict")
def predict_usingJson(item: Item):
    cat_cols=[item.Purpose,
    item.Property,
    item.Loan_history,
    item.Gender,
    item.Marital_status,
    item.Housing,
    item.Employment_status,
    item.Has_been_employed_for_at_least,
    item.Has_been_employed_for_at_most,
    item.Savings_account_balance
    ]

    selected_cols=[
        item.Months_loan_taken_for,
        item.Principal_loan_amount,
        item.Primary_applicant_age_in_years]

    X=[
        item.EMI_rate_in_percentage_of_disposable_income,
        item.Has_coapplicant,
        item.Has_guarantor,
        item.Number_of_existing_loans_at_this_bank,
        item.Number_of_dependents,
        item.Years_at_current_residence,
        item.Foreign_worker]

    oh_encoded=oh_encoder.transform([cat_cols])
    selected_val=np.log(selected_cols)
    scaled=std_scaler.transform([selected_val])

    X.extend(scaled[0])
    X.extend(oh_encoded[0])
    X=np.array(X)
    X=X.reshape(1,-1)
    pred=model.predict(X)
    if int(pred[0])==1:
        return {"prediction": "High Risk"}
    else:
        return {"prediction": "Low Risk"}


