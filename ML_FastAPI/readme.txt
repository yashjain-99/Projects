Steps to run API server:
1. Make sure you have python3 installed. Run python --version to get right version of python installed in your system.
2. open terminal into reunion directory and run "pip install -r requirements.txt" to install dependencies.
3. Run "uvicorn main:app" in terminal to start server. 
4. Open postman or visit http://127.0.0.1:8000/docs to access API page and then give a post request to http://127.0.0.1:8000/predict with JSON body having your input data.
5. Sample input data:
	{"Months_loan_taken_for": 12,
 	"Purpose": "education",
 	"Principal_loan_amount": 2096000,
 	"EMI_rate_in_percentage_of_disposable_income": 2,
 	"Property": "real estate",
 	"Has_coapplicant": 0,
 	"Has_guarantor": 0,
 	"Number_of_existing_loans_at_this_bank": 1,
 	"Loan_history": "critical/pending loans at other banks",
 	"Primary_applicant_age_in_years": 49,
 	"Gender": "male",
 	"Marital_status": "single",
 	"Number_of_dependents": 2,
 	"Housing": "own",
 	"Years_at_current_residence": 3,
 	"Employment_status": "unskilled - resident",
 	"Has_been_employed_for_at_least": "4 years",
 	"Has_been_employed_for_at_most": "7 years",
 	"Foreign_worker": 1,
 	"Savings_account_balance": "Low"}

incase of any queries reach out to : yashj133.yj@gmail.com